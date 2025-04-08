from flask import Flask, jsonify, render_template, request
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Episodes List Route
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    # Pass episodes data to the template for rendering
    return render_template('episodes_list.html', episodes=episodes)

# Episode Details Route
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404

    # Fetch appearances for the episode
    appearances = Appearance.query.filter_by(episode_id=id).all()
    return render_template('episode_details.html', episode=episode, appearances=appearances)

# Delete Episode Route
@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404

    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': f'Episode {id} deleted successfully'})

# Guests List Route
@app.route('/guests', methods=['GET'])
def guest_list():
    guests = Guest.query.all()
    return render_template('guests.html', guests=guests)

# Guest Details Route
@app.route('/guests/<int:id>', methods=['GET'])
def guest_details(id):
    guest = Guest.query.get(id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404

    appearances = Appearance.query.filter_by(guest_id=id).all()

    # Fun and quirky reasons for guests' inclusion
    funny_reasons = {
        "Jim Al-Khalili": "Jim Al-Khalili is a physicist and science talker, which means he knows all about atoms, time, and why your toast always lands butter-side down if you're already late.",
        "Laura Ashe": "Laura Ashe is a medieval literature professor, then brought in to keep us grounded in historical accuracy.",
        "Paul Bahn": "Paul Bahn is an archaeologist specializing in prehistoric art, then needed because someone needs to uncover the archaeological mystery of our agenda.",
        "Nigel Spivey": "Nigel Spivey is a classical art historian, then hired to argue why this meeting should be considered an artistic masterpiece.",
        "Shirley J. Thompson": "Shirley J. Thompson is a composer and music professor, then recruited to compose a celebratory anthem when this meeting finally ends.",
        "Irving Finkel": "Irving Finkel is an Assyriologist at the British Museum, then brought in to interpret ancient texts that somehow align with our strategy.",
        "Martin Kemp": "Martin Kemp is an art historian focusing on Leonardo da Vinci, then tasked to explain how visual art can solve our scheduling problems.",
        "Brian Klaas": "Brian Klaas is a political scientist studying democracy, then included because democracy matters, even in snack decisions.",
        "Eleanor Robson": "Eleanor Robson is an expert in ancient Mesopotamian mathematics, then hired to fact-check everything before we call it 'fake history.'",
        "Rupert Sheldrake": "Rupert Sheldrake is a biologist known for controversial theories, then asked to debate whether your ideas resonate across morphic fields.",
    }

    guest_reason = funny_reasons.get(
        guest.name,
        "To remind us of the joy of teamwork and collaboration."
    )

    # Render guest details template with all data passed
    return render_template('guest_details.html',
                           guest=guest,
                           appearances=appearances,
                           guest_reason=guest_reason)

# Create Appearance Route
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )
        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict(recurse={
            'episode': ('id', 'date', 'number'),
            'guest': ('id', 'name', 'occupation')
        })), 201
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)

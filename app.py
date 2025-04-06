from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Landing Page Route
@app.route('/')
def index():
    return render_template('index.html')

# Episode List Endpoint (Optional, Only for API Clients)
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict(only=('id', 'date', 'number')) for episode in episodes])

# Episode Details Route
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify(episode.to_dict())

@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': f'Episode {id} deleted successfully'})

# Guest List Route
@app.route('/guests', methods=['GET'])
def guest_list():
    guests = Guest.query.all()
    return render_template('guests.html', guests=guests)

@app.route('/guests/<int:id>', methods=['GET'])
def guest_details(id):
    guest = Guest.query.get(id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404

    # Add a fun reason for the guest's participation
    funny_reasons = {
        "Jim Al-Khalili": "To calculate the probability of this meeting lasting longer than expected.",
        "Laura Ashe": "To keep us grounded in historical accuracy.",
        "Paul Bahn": "Because someone needs to uncover the archaeological mystery of our agenda.",
        "Nigel Spivey": "To argue why this meeting should be considered an artistic masterpiece.",
        "Shirley J. Thompson": "To compose a celebratory anthem when this meeting finally ends.",
        "Irving Finkel": "To interpret ancient texts that somehow align with our strategy.",
        "Martin Kemp": "To explain how visual art can solve our scheduling problems.",
        "Brian Klaas": "Because democracy matters, even in snack decisions.",
        "Eleanor Robson": "To fact-check everything before we call it 'fake history.'",
        "Rupert Sheldrake": "To debate whether your ideas resonate across morphic fields.",
    }
    reason = funny_reasons.get(guest.name, "To remind us of the joy of teamwork.")

    return render_template('guest_details.html', guest=guest, reason=reason)



# Create Appearance API Endpoint
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

        return jsonify(appearance.to_dict(recurse={'episode': ('id', 'date', 'number'),
                                                   'guest': ('id', 'name', 'occupation')})), 201
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)

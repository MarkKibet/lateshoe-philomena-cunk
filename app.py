from flask import Flask, jsonify, render_template, request
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.before_request
def method_override():
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method in ['DELETE', 'PUT']:
            request.environ['REQUEST_METHOD'] = method


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return render_template('episodes_list.html', episodes=episodes)


@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404

    appearances = Appearance.query.filter_by(episode_id=id).all()
    return render_template('episode_details.html', episode=episode, appearances=appearances)

@app.route('/episodes', methods=['DELETE', 'POST'])
def delete_episode():
    episode_id = request.form.get('episode_id')
    if not episode_id:
        return jsonify({'error': 'Episode ID not provided'}), 400

    episode = Episode.query.get(episode_id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404

    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': f'Episode {episode_id} deleted successfully'})

@app.route('/manage', methods=['GET'])
def manage():
    return render_template('manage_episodes.html')


@app.route('/guests', methods=['GET'])
def guest_list():
    guests = Guest.query.all()
    return render_template('guests.html', guests=guests)


@app.route('/guests/<int:id>', methods=['GET'])
def guest_details(id):
    guest = Guest.query.get(id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404

    appearances = Appearance.query.filter_by(guest_id=id).all()

    funny_reasons = {
        
        "Jim Al-Khalili": "Jim Al-Khalili, who holds the distinguished title of physicist and professional science talker, probably knows how atoms work and everything. He probably even knows why things fall down instead of up, which is one of the biggest mysteries in science apart from why bread always lands butter-side down and how they get the filling inside Twix bars. He's here to explain quantum mechanics, which is like regular mechanics but much smaller and somehow involves cats that are both dead and alive at the same time, which sounds like animal cruelty if you ask me.",
        
        "Laura Ashe": "Laura Ashe spends her days as a professor of medieval literature at the University of Oxford, which means she reads books by people who've been dead for hundreds of years and haven't published anything new in ages. She knows all about Shakespeare's ancestors who couldn't spell as good as him and wrote stories about knights who spent their time looking for special cups instead of just buying one from the shops. She's basically a time traveler but without the actual traveling part.",
        
        "Paul Bahn": "Paul Bahn, an archaeologist whose heart beats for prehistoric art, has been summoned to enlighten us about cave paintings made by people who hadn't invented proper paper yet. He spends his life looking at ancient doodles that make modern toddlers' refrigerator art look sophisticated. For all we know, these cave paintings could just be prehistoric shopping lists or someone trying to draw their pet mammoth, but apparently they're 'culturally significant' enough for Paul to build a whole career around them.",
        
        "Nigel Spivey": "Nigel Spivey, a classical art historian so good he probably dreams in marble statues, can tell you why ancient Greek sculptures never have proper arms and why everyone in old paintings looks so miserable. He studies art from times when nobody knew how to smile in portraits and when the best special effect they had was gold leaf. Nigel probably has strong opinions about which classical sculptures have the best abs and can tell you exactly why the Mona Lisa is smiling – probably because someone told her the sitting would only take five minutes but actually it took three years.",
        
        "Shirley J. Thompson": "Shirley J. Thompson, who is a composer and music professor, has the Herculean task of creating music that doesn't sound like it's been made already. She writes classical music in a world where Beethoven and Mozart have already used all the good notes in the best order. It's like trying to invent a new color when the rainbow's already taken all the good ones. She probably sits at home surrounded by crumpled-up sheets of music paper thinking, 'Darn it, Bach, you've done it again!' Her students probably ask why they can't just add a sick beat drop to Vivaldi and call it a day.",
        
        "Irving Finkel": "Irving Finkel, an Assyriologist at the British Museum and a man who probably looks exactly like you're imagining right now, knows how to read squiggly lines pressed into clay by people thousands of years ago. He's basically a time detective who can tell you what ancient Mesopotamians were complaining about on their clay tablets – probably things like 'The River Tigris flooded again' or 'Nebuchadnezzar keeps borrowing my bronze tools and not giving them back.'",
        
        "Martin Kemp": "Martin Kemp, the art historian with a soft spot for Leonardo da Vinci, knows all about a man who spent his time drawing helicopters that wouldn't work and people with perfect proportions that make the rest of us feel inadequate. Martin can tell you exactly why the Mona Lisa is so famous despite being a rather small painting of a woman who looks like she's trying not to laugh at a joke that wasn't that funny. He probably has nightmares about The Da Vinci Code and has to resist the urge to correct strangers in museums who think all Renaissance paintings were done by either Leonardo or Michelangelo, as if they were the Batman and Robin of the art world.",
        
        "Brian Klaas": "Brian Klaas, who spends his time being a political scientist and studying democracy, has the misfortune of being an expert in something that many countries try but few get right, like soufflés or parallel parking. He analyses political systems around the world, a bit like a doctor who specializes in particularly contagious diseases. Brian can explain complex geopolitical situations using small words for the rest of us, and probably lies awake at night wondering if democracy would work better if we let dolphins vote too.",
        
        "Eleanor Robson": "Eleanor Robson, the expert on ancient Mesopotamian mathematics, knows how people did sums before calculators, computers, or even proper numbers were invented. She studies a time when counting past ten was considered advanced mathematics and when the most complex equation was probably 'If Gilgamesh has three goats and Enkidu takes one, how many epic poems will it take to get it back?' Eleanor can read ancient mathematical texts that look like someone dropped a Scrabble board, and she probably gets unreasonably excited about cuneiform tablets that turn out to be nothing more than ancient receipts for grain purchases.",
        
        "Rupert Sheldrake": "Rupert Sheldrake, a biologist best known for his delightfully controversial theories that make other scientists reach for their blood pressure medication, spends his time thinking about telepathic dogs and morphic resonance while conventional scientists try to pretend he doesn't exist. He's either a misunderstood genius centuries ahead of his time or completely wrong about everything – there's no middle ground really. Rupert probably does experiments like asking his pet terrier to predict lottery numbers and then writing serious papers about the results."
    }
 

    guest_reason = funny_reasons.get(
        guest.name,
        "To remind us of the joy of teamwork and collaboration."
    )

    return render_template('guest_details.html', guest=guest, appearances=appearances, guest_reason=guest_reason)

@app.route('/create_appearance', methods=['POST'])
def create_appearance():
    try:
        data = request.json  # 

        if not data.get('rating'):
            raise ValueError("Rating is required.")
        if not data.get('episode_id'):
            raise ValueError("Episode ID is required.")
        if not data.get('guest_id'):
            raise ValueError("Guest ID is required.")

        
        rating = int(data.get('rating'))
        episode_id = int(data.get('episode_id'))
        guest_id = int(data.get('guest_id'))

        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(appearance)
        db.session.commit()

        return jsonify({'message': 'Appearance created successfully'}), 201
    except ValueError as e:  
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:  
        return jsonify({'errors': [str(e)]}), 400


if __name__ == '__main__':
    app.run(port=5555, debug=True)

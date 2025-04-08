# Import necessary modules
from app import db
from models import Episode

# Populate the database with four episodes
episode1 = Episode(
    number=1,
    date="2025-04-01",
    description="Philomena embarks on a journey through time, space, and questionable historical decisions.",
    themes="Existence, the universe, and why history happened in the past instead of somewhere more convenient.",
    quote="Sometimes I wonder if history really happened, or if it was just something they made up to sell museum tickets.",
    fun_facts="Did you know that if you laid all the facts from this episode end to end, they would stretch from here to somewhere else entirely?"
)

episode2 = Episode(
    number=2,
    date="2025-04-08",
    description="Philomena explores how geography shaped humanity and wonders why mountains exist.",
    themes="Geography, human evolution, and the peculiarities of the Earth's design.",
    quote="Mountains are just big inconveniences. Humanity must have invented hiking just to spite geography.",
    fun_facts="If you flattened the Earth's mountains, we'd have a lot more space for parking lots."
)

episode3 = Episode(
    number=3,
    date="2025-04-15",
    description="Philomena investigates the mysterious world of art and asks why nobody painted dinosaurs.",
    themes="Art, creativity, and why ancient people couldn't figure out color palettes.",
    quote="Art is just drawing something and convincing everyone else it has meaning. Like coloring with more steps.",
    fun_facts="Did you know the Mona Lisa's smile took four years to paint? She must have been really patient!"
)

episode4 = Episode(
    number=4,
    date="2025-04-22",
    description="Philomena dives into the history of war, wondering why people couldn't settle disputes with games of chess instead.",
    themes="Conflict, strategy, and why humans are terrible at sharing.",
    quote="War is humanity's way of proving they can't play nicely with their toys.",
    fun_facts="The longest war in history lasted over 300 years but featured almost no actual fighting."
)

# Add and commit all episodes to the database
db.session.add_all([episode1, episode2, episode3, episode4])
db.session.commit()

print("Database populated with four episodes!")

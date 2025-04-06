from models import db, Guest, Episode, Appearance
from app import app

# Dropping and recreating all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    # Adding Guests
    guests = [
        Guest(name="Jim Al-Khalili", occupation="Physicist"),
        Guest(name="Laura Ashe", occupation="Historian"),
        Guest(name="Paul Bahn", occupation="Archaeologist"),
        Guest(name="Nigel Spivey", occupation="Art Historian"),
        Guest(name="Shirley J. Thompson", occupation="Composer"),
        Guest(name="Irving Finkel", occupation="Assyriologist"),
        Guest(name="Martin Kemp", occupation="Art Historian"),
        Guest(name="Brian Klaas", occupation="Political Scientist"),
        Guest(name="Eleanor Robson", occupation="Historian"),
        Guest(name="Rupert Sheldrake", occupation="Biologist"),
    ]
    db.session.add_all(guests)

    # Adding Episodes
    episodes = [
        Episode(date="2025-04-01", number=1),
        Episode(date="2025-04-02", number=2),
        Episode(date="2025-04-03", number=3),
        Episode(date="2025-04-04", number=4),
    ]
    db.session.add_all(episodes)

    # Adding Appearances (Linking Guests and Episodes)
    appearances = [
        Appearance(guest_id=1, episode_id=1, rating=5),  # Jim Al-Khalili on Episode 1
        Appearance(guest_id=2, episode_id=2, rating=4),  # Laura Ashe on Episode 2
        Appearance(guest_id=3, episode_id=3, rating=5),  # Paul Bahn on Episode 3
        Appearance(guest_id=4, episode_id=1, rating=3),  # Nigel Spivey on Episode 1
        Appearance(guest_id=5, episode_id=2, rating=5),  # Shirley J. Thompson on Episode 2
        Appearance(guest_id=6, episode_id=3, rating=4),  # Irving Finkel on Episode 3
        Appearance(guest_id=7, episode_id=4, rating=5),  # Martin Kemp on Episode 4
        Appearance(guest_id=8, episode_id=4, rating=4),  # Brian Klaas on Episode 4
        Appearance(guest_id=9, episode_id=1, rating=3),  # Eleanor Robson on Episode 1
        Appearance(guest_id=10, episode_id=2, rating=4), # Rupert Sheldrake on Episode 2
    ]
    db.session.add_all(appearances)

    # Committing to the database
    db.session.commit()

    print("Database seeded successfully!")

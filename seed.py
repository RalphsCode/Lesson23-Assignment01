""" Seed File to populate the pets Table in the adopt database """

from models import Pet, db
from app import app

# Drop & Create the table
with app.app_context():
    db.drop_all()
    db.create_all()

# If table isn't empty, empty it
with app.app_context():
    Pet.query.delete()

# Create Pet Objects
ralphie = Pet(name="Ralphie", species="dog", photo_url="https://images.unsplash.com/photo-1518887499460-71d222eed89d?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGV0c3xlbnwwfHwwfHx8MA%3D%3D", age=3, notes="Very playful, loves kids!")

rover = Pet(name="Rover", species="dog", photo_url="https://plus.unsplash.com/premium_photo-1669234115921-8c5e7bbd2654?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8cGV0c3xlbnwwfHwwfHx8MA%3D%3D", age=5, notes="Relaxed Nature. Loves to play fetch. Great swimmer!")

mittens = Pet(name="Mittens", species="cat", photo_url="https://images.unsplash.com/photo-1472491235688-bdc81a63246e?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", age=2, notes="Very Curious Cat!")

spike = Pet(name="Spike", species="porcupine", photo_url="https://plus.unsplash.com/premium_photo-1664302959064-6c3e5fb92fc6?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cG9yY3VwaW5lfGVufDB8fDB8fHww", notes="Not suitable for homes with young children!")


# Add the pets
with app.app_context():
    db.session.add_all([ralphie, rover, mittens, spike])
    db.session.commit()
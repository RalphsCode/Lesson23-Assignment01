""" Adopt A PET Project - Lesson 23 - Assignment01 """

# IMPORTS
from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet
from forms import AddPet

# Define the App
app = Flask(__name__)  # creating an instance of the Flask Class

# Debug configuration
app.config['SECRET_KEY'] = "RalphsCode-123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ponderosa@localhost/adopt'
app.config['SQLALCHEMY_RECORD_QUERIES'] = False
app.config['SQLALCHEMY_ECHO'] = True

with app.app_context():
    connect_db(app)
    db.create_all()

###  ROUTES  ###
@app.route('/')
def home():
    """ App Home Page """
    all_pets = Pet.query.all()
    return render_template('home.html', all_pets=all_pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Page with a form to add a new pet to the database """
    form = AddPet()
    if form.validate_on_submit(): # only works on the post request
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = True

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        with app.app_context():
            db.session.add(new_pet)
            db.session.commit()

        flash(f"New {species}; {name} Added Successfully.")
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)
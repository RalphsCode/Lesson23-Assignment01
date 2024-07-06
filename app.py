""" Adopt A PET Project - Lesson 23 - Assignment01 """

# IMPORTS
from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet

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
    all_pets = Pet.query.all()
    return render_template('home.html', all_pets=all_pets)
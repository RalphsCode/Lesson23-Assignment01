""" Models for the Adopt App & Database """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  		

#Put the connection in a function so it doesn't run immediately and unnecessarily.
def connect_db(app):
        db.app = app  			# associate flask app with the db variable
        db.init_app(app)   		# initialize

#### MODELS BELOW ####

class Pet(db.Model):
        """ The Pet Table in the db"""

        __tablename__= "pets"

        id = db.Column(db.Integer, primary_key= True, autoincrement=True)

        name = db.Column(db.String(50), nullable=False)

        species = db.Column(db.String(50), nullable=False) 

        photo_url = db.Column(db.String(250), nullable=True)

        age =  db.Column(db.Integer, nullable=True)

        notes = db.Column(db.String(250), nullable=True)

        available = db.Column(db.Boolean, default=True, nullable=False)

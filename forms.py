""" WTForms for the Pet Adoption Website """

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField, validators

class AddPet(FlaskForm):
    """ Creates a pet and adds it to the database. """
    name = StringField("Pet Name", validators=[validators.InputRequired()])

    species = SelectField("Species", choices=(['cat', 'Cat'], ['dog', 'Dog'], ['porcupine', 'Porcupine']))
    
    photo_url = StringField("URL for Pet Photo", validators=[validators.optional(), validators.URL(message="Please enter a valid URL")])
    
    age = IntegerField('Age in years', validators=[validators.optional(), validators.NumberRange(min=0, max=30)])
    
    notes = TextAreaField('Pet Notes')


class EditPet(FlaskForm):
    """ Edit some details about an existing pet """
    photo_url = StringField("URL for Pet Photo", validators=[validators.optional(), validators.URL(message="Please enter a valid URL")])
    
    notes = TextAreaField('Pet Notes')

    available = BooleanField('Available')
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField

class AddPet(FlaskForm):
    name = StringField("Pet Name")
    species = SelectField("Species", choices=(['cat', 'Cat'], ['dog', 'Dog'], ['porc', 'Porcupine']))
    photo_url = StringField("URL for Pet Photo")
    age = IntegerField('Age in years')
    notes = TextAreaField('Pet Notes')
    
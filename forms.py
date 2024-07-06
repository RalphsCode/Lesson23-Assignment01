from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, validators

class AddPet(FlaskForm):
    name = StringField("Pet Name", validators=[validators.InputRequired()])
    species = SelectField("Species", choices=(['cat', 'Cat'], ['dog', 'Dog'], ['porc', 'Porcupine']))
    photo_url = StringField("URL for Pet Photo")
    age = IntegerField('Age in years', validators=[validators.optional()])
    notes = TextAreaField('Pet Notes')
    
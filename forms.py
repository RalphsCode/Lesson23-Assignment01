from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, validators

class AddPet(FlaskForm):
    
    name = StringField("Pet Name", validators=[validators.InputRequired()])

    species = SelectField("Species", choices=(['cat', 'Cat'], ['dog', 'Dog'], ['porcupine', 'Porcupine']))
    
    photo_url = StringField("URL for Pet Photo", validators=[validators.optional(), validators.URL()])
    
    age = IntegerField('Age in years', validators=[validators.optional(), validators.NumberRange(min=0, max=30)])
    
    notes = TextAreaField('Pet Notes')
    
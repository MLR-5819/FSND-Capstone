from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class AddEntryForm(FlaskForm):
    # Add new entry form
    name = TextField('Entry Name:', [DataRequired(), Length(max=16, message=('Your title is too long.'))])
    category = SelectField('Choose a Category:', coerce=int)
    url = TextField('Photo URL Link:', [DataRequired()])
    submit = SubmitField('Submit')
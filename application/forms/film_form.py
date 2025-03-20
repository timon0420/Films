from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class FilmForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(
        min=5, max=100
    )])
    film_genre = StringField(validators=[InputRequired(), Length(
        min=5, max=100
    )])
    film_status = RadioField(validators=[InputRequired()], choices=['watched', 'to watch'])
    film_type = RadioField(validators=[InputRequired()], choices=['film', 'series'])
    submit = SubmitField("Add")
    
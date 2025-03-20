from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError
from application.model import Users

class Form(FlaskForm):
    login = StringField(validators=[InputRequired(), Length(
        min=4, max=20
    )], render_kw={"placehoder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20
    )], render_kw={"placeholder": "Password"})
    
class RegistrationForm(Form):
    email = EmailField(validators=[InputRequired(), Length(
        min=10, max= 40
    )], render_kw={"placeholder": "Email"})
    submit = SubmitField("Register")

    def validate_user(self, login):
        existing_user_login = Users.query.filter_by(login=login.data).first()
        if existing_user_login:
            raise ValidationError(
                "That login is already exists. Pleace choose a diffrent one."
            )
        
class LoginForm(Form):
    submit = SubmitField("Login")

    def validate_user(self, login):
        existing_user_login = Users.query.filter_by(login=login.data).first()
        if not existing_user_login:
            raise ValidationError(
                "That login is not yet available."
            )
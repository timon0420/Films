from flask import render_template, url_for, redirect, session, request, flash 
from application.model import Users
from application import db, app, bcrypt, csrf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_login import login_user, login_required, logout_user

class RegistrationForm(FlaskForm):
    login = StringField(validators=[InputRequired(), Length(
        min=4, max=20
    )], render_kw={"placehoder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20
    )], render_kw={"placehoder": "Password"})
    email = EmailField(validators=[InputRequired(), Length(
        min=10, max= 40
    )], render_kw={"placehoder": "Email"})
    submit = SubmitField("Register")

    def validate_user(self, login):
        existing_user_login = Users.query.filter_by(login=login.data).first()
        if existing_user_login:
            raise ValidationError(
                "That login is already exists. Pleace choose a diffrent one."
            )
        
class LoginForm(FlaskForm):
    login = StringField(validators=[InputRequired(), Length(
        min=4, max=20
    )], render_kw={"placehoder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20
    )], render_kw={"placehoder": "Password"})
    submit = SubmitField("Login")

    def validate_user(self, login):
        existing_user_login = Users.query.filter_by(login=login.data).first()
        if existing_user_login:
            raise ValidationError(
                "That login is already exists. Pleace choose a diffrent one."
            )

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(login=form.login.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                return redirect('/film')
            else:
                flash('Niepoprawne hasło')
                return redirect('/sign_in')
        else:
            flash('Nie znaleziono użytkownika o takich danych')
            return redirect('/sign_in')
    return render_template('sign_in.html', form=form)
    

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(login=form.login.data, password=hashed_password, mail=form.email.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/sign_in')
        except:
            return redirect('/')
    return render_template('sign_up.html', form=form)
   
@app.route('/logout')
@login_required
def logout():
   logout_user()
   return redirect('/') 
    
     
@app.route('/password_recovery', methods=['POST', 'GET'])
def password_recovery():
    if request.method == 'POST':
        login = request.form['login']
        mail = request.form['mail']
        if Users.query.filter_by(login=login, mail=mail).first() is not None:
            return redirect('/sign_in')
        else:
            flash('something went wrong if You forgot my password')
            return redirect('/password_recovery')
    else:
        return render_template('password_recovery.html')
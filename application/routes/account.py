from flask import render_template, url_for, redirect, request, flash 
from application.model import Users
from application import db, app, bcrypt, csrf
from flask_login import login_user, login_required, logout_user
from application.forms.account_form import RegistrationForm, LoginForm

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
    
     
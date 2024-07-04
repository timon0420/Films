from flask import render_template, url_for, redirect, session, request, flash 
from application.data_validation import password_validator, login_validator
from application.model import Users, Films, Films_Users
from application import db, app

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        user_login = request.form['login_sign_in']
        user_password = request.form['password_sign_in']
        found_user = Users.query.filter_by(login=user_login, password=user_password).first()
        if found_user is not None and password_validator(user_password) and login_validator(user_login):
            session['user'] = user_password
            return redirect('/film')
        else:
            flash('something went wrong if You forgot my password')
            flash('click here')
            return redirect('/sign_in')
    else:
        return render_template('sign_in.html')
    

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_login = request.form['login_sign_up']
        user_password = request.form['password_sign_up']
        user_mail = request.form['mail']
        if password_validator(user_password) and login_validator(user_login):
            try:
                user = Users(login=user_login, password=user_password, mail=user_mail)
                db.session.add(user)
                db.session.commit()
                return redirect('/sign_in')
            except:
                return render_template('sign_up.html')
        else:
            return 'NIEPOPRAWNE DANE'
    else:
        return render_template('sign_up.html')
   
@app.route('/logout')
def logout():
    try:
        session['user'] = ''
        return redirect('/')
    except:
        return "ERROR"
    
     
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
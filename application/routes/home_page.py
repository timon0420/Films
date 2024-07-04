from flask import render_template, session, redirect
from application import db, app

@app.route('/')
def login_or_registration():
    try:
        if session['user'] != '':
            return redirect('/film')
        else:
            return render_template('index.html')
    except:
        return render_template('index.html')
    
@app.route('/information')
def information():
    return render_template('information.html')
from flask import render_template, redirect
from flask_login import current_user
from application import app

@app.route('/')
def login_or_registration():
    return render_template('index.html')
    
@app.route('/information')
def information():
    return render_template('information.html')
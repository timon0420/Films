from application import app, db, bcrypt
from application.model import Users
from flask import redirect
from flask_login import logout_user
@app.route('/admin')
def admin():
    logout_user()
    return redirect('/')
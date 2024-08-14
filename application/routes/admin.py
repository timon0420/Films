from application import app, db, bcrypt
from application.model import Users
from flask import redirect
from flask_login import logout_user
@app.route('/admin')
def admin():
    # password = 'Szy04med20'
    # hashed_password = bcrypt.generate_password_hash(password)
    # user = Users.query.filter_by(login='Szymon', mail='medelaszymon@gmail.com').first()
    # if user:
    #     user.password = hashed_password
    #     try:
    #         db.session.add(user)
    #         db.session.commit()
    #     except Exception as e:
    #         return str(e)
    logout_user()
    return redirect('/')
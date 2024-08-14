from application import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False, unique=True)
    mail = db.Column(db.String(200), nullable=False, unique=True)
    
    def __init__(self, login, password, mail):
        self.login = login
        self.password = password
        self.mail = mail

class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    film_genre = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)

    def __init__(self, title, film_genre, type):
        self.title = title
        self.film_genre = film_genre
        self.type = type

class Films_Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    id_film = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, id_user, id_film, status):
        self.id_user = id_user
        self.id_film = id_film
        self.status = status

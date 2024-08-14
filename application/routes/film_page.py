from flask import render_template, url_for, redirect, session, request, flash 
from application.data_validation import  film_title_validator, film_genre_validator
from application.model import Users, Films, Films_Users
from application import db, app
from flask_login import current_user, logout_user
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

@app.route('/film', methods=['GET', 'POST'])
def film():
    form = FilmForm()
    try:
        id = current_user.id
    except:
        logout_user()
        return redirect('/')
    try:
        if form.validate_on_submit():
            title = form.title.data.capitalize()
            film_genre = form.film_genre.data.capitalize()
            try:
                film_status = form.status.data.capitalize()
                if film_status == '':
                    film_status = 'watched'.capitalize()                        
            except:
                film_status = 'watched'.capitalize()
            
            try:
                type = form.type.data.capitalize()
                if type == '':
                    type = 'film'.capitalize()
            except:
                type = 'film'.capitalize()

            if film_title_validator(title) and film_genre_validator(film_genre):
                if Films.query.filter_by(title=title, type=type).first() is None:
                    film = Films(title=title, film_genre=film_genre, type=type)
                    db.session.add(film)
                    db.session.commit()
                    films_users = Films_Users(id_user=id, id_film=film.id, status=film_status)
                    db.session.add(films_users)
                    db.session.commit()
                else:
                    film = Films.query.filter_by(title=title, film_genre=film_genre, type=type).first()
                    films_users = Films_Users(id_user=id, id_film=film.id, status=film_status)
                    db.session.add(films_users)
                    db.session.commit()
                return redirect('/film')
            else:
                return redirect('/film')
        else:
            return render_template('film.html', user_id=id, Users=Users, Films=Films, Films_Users=Films_Users, form=form)
    except:
        return redirect('/')
    
@app.route('/delete/<int:id>')
def delete_film(id):
    user = Users.query.filter_by(login=current_user.login).first()
    film = Films_Users.query.filter_by(id_user=user.id, id_film=id).first()
    try:
        db.session.delete(film)
        db.session.commit()
        return redirect('/film')
    except:
        return "ERROR <a href='/film'>Back</a>" 
    
@app.route('/changeStatus/<int:id>', methods=['POST', 'GET'])
def update_film(id):
    film_status = Films_Users.query.filter_by(id_film=id).first()
    if film_status.status == 'Watched':
        film_status.status = 'To watch'
    else:
        film_status.status = 'Watched'
    try:
        db.session.commit()
        return redirect('/film')
    except:
        return "ERROR <a href='/film'>Back</a>"

@app.route('/statistics')
def statistics():
    try:
        user_id = current_user.id
    except:
        logout_user()
        return redirect('/')
    film_genre_list = list(set([Films.query.filter_by(id=film.id_film).first().film_genre for film in Films_Users.query.filter_by(id_user=user_id).all() ]))
    number_of_films = 0
    number_of_series = 0
    for film in Films_Users.query.filter_by(id_user = user_id).all():
        type = Films.query.filter_by(id=film.id_film).first().type.lower()
        if type == 'film': number_of_films += 1
        else: number_of_series += 1
    return render_template('statistics.html', id=user_id, Users=Users, Films=Films, Films_Users=Films_Users, film_genre_list=film_genre_list, number_of_films=number_of_films, number_of_series=number_of_series, number_of_all=number_of_films+number_of_series)

@app.route('/search/<int:id>')
def search(id):
    return str(id)
    
    


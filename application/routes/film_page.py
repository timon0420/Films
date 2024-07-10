from flask import render_template, url_for, redirect, session, request, flash 
from application.data_validation import  film_title_validator, film_genre_validator
from application.model import Users, Films, Films_Users
from application import db, app
from flask_login import current_user

@app.route('/film', methods=['GET', 'POST'])
def film():
    try:
        user = Users.query.filter_by(login=current_user.login).first()
        user_id = user.id
        if request.method == 'POST':
            title = request.form['title'].capitalize()
            film_genre = request.form['film_genre'].capitalize()
            try:
                film_status = request.form['status'].capitalize()
                if film_status == '':
                    film_status = 'watched'.capitalize()                        
            except:
                film_status = 'watched'.capitalize()
            
            try:
                type = request.form['type'].capitalize()
                if type == '':
                    type = 'film'.capitalize()
            except:
                type = 'film'.capitalize()

            if film_title_validator(title) and film_genre_validator(film_genre):
                if Films.query.filter_by(title=title, type=type).first() is None:
                    film = Films(title=title, film_genre=film_genre, type=type)
                    db.session.add(film)
                    db.session.commit()
                    films_users = Films_Users(id_user=user_id, id_film=film.id, status=film_status)
                    db.session.add(films_users)
                    db.session.commit()
                else:
                    film = Films.query.filter_by(title=title, film_genre=film_genre, type=type).first()
                    films_users = Films_Users(id_user=user_id, id_film=film.id, status=film_status)
                    db.session.add(films_users)
                    db.session.commit()
                return redirect('/film')
            else:
                return redirect('/film')
        else:
            return render_template('film.html', user_id=user_id, Users=Users, Films=Films, Films_Users=Films_Users)
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
    user_id = Users.query.filter_by(password=session['user']).first().id
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
    
    


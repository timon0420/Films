import re
def password_validator(password):
    return True if re.match(r'.*[1-9]+.*', password) and re.match(r'.*[a-z]+.*', password) and re.match(r'.*[A-Z]+.*', password) and len(password) > 5 else False
def login_validator(login):
    return True if re.match(r'[a-z]+[1-9]*', login, re.IGNORECASE) and len(login) > 5 else False
def film_title_validator(title):
    return True if re.match(r'.*[a-z]+.*', title, re.IGNORECASE) and re.match(r'.*[1-9]*.*', title) else False
def film_genre_validator(film_genre):
    return True if re.match(r'.*[a-z]+.*', film_genre, re.IGNORECASE) else False
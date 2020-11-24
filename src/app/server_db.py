from flask import Flask, Response, request
from entities.trophies_entity import TrophyList
from flask_cors import CORS, cross_origin
from entities.rating_entity import Rating
from entities.leisures_entity import LeisureList
from entities.user_entity import User

import json

app = Flask(__name__)
mimetype = 'application/json'


leisures_type = [
    'MUSEUM',
    'ARTGALLERY',
    'DOGPARK',
    'MONUMENT',
    'TRAINING',
    'LIBRARY',
    'CINEMA',
    'THEATER'
]


@app.errorhandler(404)
def not_found():
    return Response(json.dumps({'error': 'Not found'}), mimetype=mimetype, status=404)


# CREATE
@app.route('/users/create/user', methods=['POST'])
def create_user():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    user = User.search_by_email(email)
    status = 200
    if not isinstance(user, dict):
        User(email=email, username=username, password=password)
        result = {'result': f'Status 200. The user was created.'}
    else:
        status = 400
        result = {'error': f'Error 400. The user with Email: {email} is already in the database'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/ratings/create/rating', methods=['POST'])
def create_rating():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    user_key = request.json['user']
    leisure_id = request.json['leisure']
    grade = request.json['grade']
    text = request.json['text']
    user = User.search_by_key(user_key)
    leisure = ''
    for leisure_type in leisures_type:
        ls = LeisureList(leisure_type)
        leisure = ls.get_by_id(leisure_id)
        print(leisure)
        if isinstance(leisure, dict):
            break
    status = 200
    if isinstance(user, dict) and isinstance(leisure, dict) and 5 >= grade >= 0:
        rating = Rating.search_by_user_and_leisure(user_key, leisure_id)
        if not isinstance(rating, dict):
            result = Rating(user_key, leisure_id, grade, text)
        else:
            status = 400
            result = f'Error 400. The rating with user_key:{user_key} and Leisure_ID:{leisure_id} is already in the ' \
                     f'database. '
    else:
        status = 400
        result = f'Error 400. The user_key:{user_key} or Leisure_ID:{leisure_id} is wrong or does not exists in the ' \
                 f'system. '

    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/trophies/create/trophy')
def create_trophies():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    trophy_name = request.json['name']
    text = request.json['text']
    trophy = TrophyList.search_by_name(trophy_name)
    status = 200
    if not isinstance(trophy, dict) and text is not None:
        result = TrophyList(trophy_name, text)
    else:
        status = 400
        result = {'error': f'Error 400. The trophy: {trophy_name} is already in the database.'}

    return Response(json.dumps(result), mimetype=mimetype, status=status)


# GET

@app.route('/users/username/<string:username>')
def get_user_by_username(username):
    user = User.search_by_username(username)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User: {username} not found'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/users/email/<string:email>')
def get_user_by_email(email):
    user = User.search_by_email(email)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User with email: {email} not found'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/users/user_key/<string:user_key>')
def get_user_by_user_key(user_key):
    user = User.search_by_key(user_key)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User with id: {user_key} not found'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/ratings/user/<string:user_key>')
def get_ratings_by_user(user_key):
    user = User.search_by_key(user_key)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User with id: {user_key} not found'
        return Response(json.dumps(user), mimetype=mimetype, status=status)
    else:
        ratings = Rating.search_by_user(user_key)
        if not bool(ratings):
            status = 404
            ratings = f'Error 404. User with id: {user_key} has not ratings yet'
    return Response(json.dumps(ratings), mimetype=mimetype, status=status)


@app.route('/ratings/leisure/<int:leisure_id>')
def get_ratings_by_leisure(leisure_id):
    for leisure_type in leisures_type:
        leisure = LeisureList(leisure_type).get_by_id(leisure_id)
        status = 200
        if not isinstance(leisure, dict):
            status = 404
            leisure = f'Error 404. Leisure with id: {leisure_id} not found'
            return Response(json.dumps(leisure), mimetype=mimetype, status=status)
        else:
            ratings = Rating.search_by_leisure(leisure['id'])
            if not bool(ratings):
                status = 404
                ratings = f'Error 404. Leisure with id: {leisure_id} has not ratings yet'
        return Response(json.dumps(ratings), mimetype=mimetype, status=status)


@app.route('/trophies/<string:name>')
def get_trophies_by_name(name):
    trophy = TrophyList.search_by_name(name)
    status = 200
    if not isinstance(trophy, dict):
        status = 404
        trophy = f'Error 404. Trophy with name: {name} not found'
    return Response(json.dumps(trophy), mimetype=mimetype, status=status)


# UPDATE


@app.route('/users/update/user/username', methods=['PUT'])
def update_user_username():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    user_key = request.json['user']
    username = request.json['username']
    status = 200
    if user_key is not None and username is not None:
        user = User(user_key)
        user.set_username(username)
    else:
        status = 404
        user = {'Error': f'Error 404. User with key: {user_key} not found and cannot be updated'}
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/users/update/user/password', methods=['PUT'])
def update_user_password():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    user_key = request.json['user']
    password = request.json['password']
    status = 200
    if user_key is not None and password is not None:
        user = User(user_key)
        user.set_password(password)
    else:
        status = 400
        user = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/ratings/update/rating/grade', methods=['PUT'])
def update_rating_grade():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    rating_key = request.json['rating']
    grade = request.json['grade']
    status = 200
    if rating_key is not None and grade is not None:
        if 5 >= grade >= 0:
            rating = Rating(rating_key)
            rating.set_grade(grade)
        else:
            rating = {'Error': f'Error 400. Grade must be between 0 and 5 for rating: {rating_key}'}
            status = 400
    else:
        status = 400
        rating = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(rating), mimetype=mimetype, status=status)


@app.route('/ratings/update/rating/text', methods=['PUT'])
def update_rating_text():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    rating_key = request.json['rating']
    text = request.json['text']
    status = 200
    if rating_key is not None and text is not None:
        rating = Rating(rating_key)
        rating.set_text(text)
    else:
        status = 400
        rating = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(rating), mimetype=mimetype, status=status)


@app.route('/trophies/update/trophy/name', methods=['PUT'])
def update_trophy_name():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    trophy_key = request.json['trophy']
    name = request.json['name']
    status = 200
    if trophy_key is not None and name is not None:
        trophy = TrophyList(trophy_key)
        trophy.set_name(name)
    else:
        status = 400
        trophy = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(trophy), mimetype=mimetype, status=status)


@app.route('/trophies/update/trophy/text', methods=['PUT'])
def update_trophy_text():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    trophy_key = request.json['trophy']
    text = request.json['text']
    status = 200
    if trophy_key is not None and text is not None:
        trophy = TrophyList(trophy_key)
        trophy.set_text(text)
    else:
        status = 400
        trophy = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(trophy), mimetype=mimetype, status=status)


# DELETE

@app.route('/users/delete/user', methods=['DELETE'])
def delete_user_by_id():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    user_key = request.json['user']
    user = User().search_by_key(user_key)
    status = 200
    if user_key is not None and isinstance(user, dict):
        User().delete(user_key)
    else:
        status = 400
        user = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/ratings/delete/rating', methods=['DELETE'])
def delete_rating_by_id():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    rating_key = request.json['rating']
    rating = Rating().search_by_id(rating_key)
    status = 200
    if rating is not None and isinstance(rating, dict):
        Rating().delete(rating_key)
    else:
        status = 400
        rating = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(rating), mimetype=mimetype, status=status)


@app.route('/trophies/delete/trophy', methods=['DELETE'])
def delete_trophy_by_id():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    trophy_key = request.json['trophy']
    trophy = TrophyList.search_by_trophy_key(trophy_key)
    status = 200
    if trophy is not None:
        TrophyList.delete(trophy_key)
    else:
        status = 400
        trophy = {'Error': f'Error 400. Bad request. The provided data is not correct.'}
    return Response(json.dumps(trophy), mimetype=mimetype, status=status)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=30006, debug=True)

from flask import Flask, Response
from entities import user_entity, rating_entity, trophies_entity, leisures_entity
import json
app = Flask(__name__)
mimetype = 'application/json'


# CREARENTIDADES
@app.route('/users/<string:email>/<string:username>/<string:password>')
def create_user(email, username, password):
    user = user_entity.User.search_by_email(email)
    status = 200
    result = ''
    if not isinstance(user, dict):
        result = user_entity.User(email, username, password)
    else:
        status = 400
        result = f'Error 400. The user with Email:{email} is already in the database'

    return Response(json.dumps(result),mimetype=mimetype, status=status)


@app.route('/rating/<string:user_id>/<int:leisure_id>/<int:grade>/<string:text>')
def create_rating(user_id, leisure_id, grade, text):
    user = user_entity.User.search_by_id(user_id)
    leisure = leisures_entity.LeisureList.get_by_id(leisure_id)
    status = 200
    result = ''
    if not isinstance(user, dict) and not isinstance(leisure, dict) and 5 >= grade >= 0:
        rating = rating_entity.Rating.search_by_user_and_leasure(user_id, leisure_id)
        if not isinstance(rating, dict):
            result = rating_entity.Rating(user_id, leisure_id, grade, text)
        else:
            status = 400
            result = f'Error 400. The rating with User_ID:{user_id} and Leisure_ID:{leisure_id} is already in the database.'
    else:
        status = 400
        result = f'Error 400. The User_ID:{user_id} or Leisure_ID:{leisure_id} is wrong or does not exists in the system.'

    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/trophy/<string:trophy_name>/<string:text>')
def create_trophies(trophy_name, text):
    trophy = trophies_entity.TrophyList.search_by_name(trophy_name)
    status = 200
    result = ''
    if not isinstance(trophy, dict):
        result = trophies_entity.TrophyList(trophy_name, text)
    else:
        status = 400
        result = f'Error 400. The trophy: {trophy_name} is already in the database.'

    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/users/<string:username>')
def get_user_by_username(username):
    user = user_entity.User.search_by_username(username)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User: {username} not found'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/users/<string:email>')
def get_user_by_email(email):
    user = user_entity.User.search_by_email(email)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User with email: {email} not found'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/users/<string:user_id>')
def get_user_by_user_id(user_id):
    user = user_entity.User.search_by_user_id(user_id)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User with id: {user_id} not found'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/ratings/<string:user_id>')
def get_ratings_by_user(user_id):
    user = user_entity.User.search_by_user_id(user_id)
    status = 200
    if not isinstance(user, dict):
        status = 404
        user = f'Error 404. User with id: {user_id} not found'
        return Response(json.dumps(user), mimetype=mimetype, status=status)
    else:
        ratings = rating_entity.Rating.search_by_user(user_id)
        if not bool(ratings):
            status = 404
            ratings = f'Error 404. User with id: {user_id} has not ratings yet'
    return Response(json.dumps(ratings), mimetype=mimetype, status=status)


@app.route('/ratings/<int:leisure_id>')
def get_ratings_by_leisure(leisure_id):
    leisure = leisures_entity.LeisureList.get_by_id(leisure_id)
    status = 200
    if not isinstance(leisure, dict):
        status = 404
        leisure = f'Error 404. Leisure with id: {leisure_id} not found'
        return Response(json.dumps(leisure), mimetype=mimetype, status=status)
    else:
        ratings = rating_entity.Rating.search_by_leisure(leisure)
        if not bool(ratings):
            status = 404
            ratings = f'Error 404. Leisure with id: {leisure_id} has not ratings yet'
    return Response(json.dumps(ratings), mimetype=mimetype, status=status)


@app.route('/trophies/<string:name>')
def get_trophies_by_name(name):
    trophy = trophies_entity.TrophyList.search_by_name(name)
    if not isinstance(trophy, dict):
        status = 404
        trophy = f'Error 404. Trophy with name: {name} not found'
    return Response(json.dumps(trophy), mimetype=mimetype, status=status)

# UPDATE


@app.route('/users/update/<string:user_id>/<string:username>', methods=['PUT'])
def update_user_username(user_id, username):
    user = user_entity.User(user_id)
    status = 200
    if user is not None:
        user.set_username(username)
    else:
        status = 404
        user = f'Error 404. User with user_id: {user_id} not found and cannot be updated'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/users/update/<string:user_id>/<string:password>', methods=['PUT'])
def update_user_password(user_id, password):
    user = user_entity.User(user_id)
    status = 200
    if user is not None:
        user.set_password(password)
    else:
        status = 404
        user = f'Error 404. User with user_id: {user_id} not found and cannot be updated'
    return Response(json.dumps(user), mimetype=mimetype, status=status)


@app.route('/ratings/update/<string:rating_id>/<int:grade>', methods=['PUT'])
def update_rating_grade(rating_id, grade):
    rating = rating_entity.Rating(rating_id)
    status = 200
    if rating is not None:
        if 5 >= grade >= 0:
            rating.set_grade(grade)
        else:
            rating = f'Error 404. Grade must be between 0 and 5 for rating: {rating_id}'
            status = 404
    else:
        status = 404
        rating = f'Error 404. Rating with rating_id: {rating_id} not found and cannot be updated'
    return Response(json.dumps(rating), mimetype=mimetype, status=status)


@app.route('/ratings/update/<string:rating_id>/<string:text>', methods=['PUT'])
def update_rating_text(rating_id, text):
    rating = rating_entity.Rating(rating_id)
    status = 200
    if rating is not None:
        rating.set_text(text)
    else:
        status = 404
        rating = f'Error 404. Rating with rating_id: {rating_id} not found and cannot be updated'
    return Response(json.dumps(rating), mimetype=mimetype, status=status)


@app.route('/trophies/update/<string:trophy_id>/<string:name>', methods=['PUT'])
def update_trophy_name(trophy_id, name):
    trophy = trophies_entity.TrophyList(trophy_id)
    status = 200
    if trophy is not None:
        trophy.set_name(name)
    else:
        status = 404
        trophy = f'Error 404. Trophy with trophy_id: {trophy_id} not found and cannot be updated'
    return Response(json.dumps(trophy), mimetype=mimetype, status=status)


@app.route('/trophies/update/<string:trophy_id>/<string:text>', methods=['PUT'])
def update_trophy_text(trophy_id, text):
    trophy = trophies_entity.TrophyList(trophy_id)
    status = 200
    if trophy is not None:
        trophy.set_text(text)
    else:
        status = 404
        trophy = f'Error 404. Trophy with trophy_id: {trophy_id} not found and cannot be updated'
    return Response(json.dumps(trophy), mimetype=mimetype, status=status)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=30006, debug=True)

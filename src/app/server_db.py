from flask import Flask, jsonify, request

from src.app import opendata

app = Flask(__name__)

#CREATE
@app.route('/users', methods=['POST'])
def create_user():
    id = request.json['id']
    #complete with entity attributes

#GET
@app.route('/users/<string:username>', methods =['GET'])
def get_user_by_username(username):
    users_found = [
        user for user in users if user['username'] == username.upper()]
    if(len(users_found)>0):
        return jsonify({'user': users_found[0]})
    return jsonify({'message': 'User Not Found'})

#UPDATE
@app.route('/users/<string: username', methods=['PUT'])
def edit_username(username):
    users_found = [
        user for user in users if user['name'] == username
    ]
    if (len(users_found)>0):
        users_found[0]['username'] = request.json['username']
        #complete with entity attributes
        return jsonify({
            'message':'User Updated',
            'user' : users_found[0]
        })
    return jsonify({'message': 'User Not Found'})

#DELETE
@app.route('/users/<string:username>', methods=['DELETE'])
def deleteProduct(username):
    users_found = [
        user for user in users if user['name'] == username
    ]
    if (len(users_found) > 0):
        users.remove(users_found[0])
        return jsonify({
            'message' : 'User Deleted',
            'users' : users
        })
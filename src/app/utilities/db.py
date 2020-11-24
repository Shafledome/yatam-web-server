import pyrebase
import os
import json
from dotenv import load_dotenv

load_dotenv()
config = json.loads(os.getenv('config'))

firebase = pyrebase.initialize_app(config)

db = firebase.database()

'''
How no relational DB works and how to use pyrebase:
There is no select from multiple tables
There is no delete/update with multiple data
    data = {
        "name": "sera"
        "username": "seraa"
        "email": "sera@sera.com"
        } 
    - db.child("users").push(data)
    It will insert a new child in the database called "users" if it does not exists, next will ad a new random key
    and insert all the data to it as a child.

    - db.child("users").child("SeraKey").set(data)
    It will create our own key and add data

    - db.child("users").child("SeraKey").update({"name": "evil sera"})
    To update data for an existing entry
    - db.child("users").child("SeraKey").remove()
    To delete data from existing entry

    - data {
        "users/SeraKey/": {
            "name": "sera"
        },
        "users/FraniKey/": {
            "name": "frani"
        }
    }
    db.update(data)
    To multi-location update

    - users = db.child("users").get()
    print(users.val())
    Returns the value of the requested data

    - users = db.child("users").get()
    print(users.key())
    Returns the key of the requested data

    - users = db.child("users").get()
    for user in users.each():
        print(user.key())
        print(user.val())
    Returns list of objects

    - users_by_name = db.child("users").order_by_child("name").get()
    This query will return users ordered by name

    - users_by_score = db.child("users").order_by_child("score").equal_to(10).get()
    This query will return users with a score of 10

    - users_by_score = db.child("users").order_by_child("score").start_at(3).end_at(10).get()
    This query returns users ordered by score and with score between 3 and 10

    - users_by_score = db.child("users").order_by_child("score").limit_to_first(5).get()
    This query returns the first five users ordered by score. You can use limit_to_last.

    - users_by_value = db.child("users").order_by_value().get()
    This query returns data ordered by their value

    - users_by_key = db.child("users").order_by_key().get
    This query returns data ordered by their key

'''


# e.g get(user) returns a dictionary
# e.g get(user, order=order) returns an ordered dictionary
def get_dict(entry, order=None):
    d = None
    if order is not None:
        d = db.child(entry).order_by_child(order).get().val()
    else:
        d = db.child(entry).get().val()
    return d


def create(entry, data):
    db.child(entry).push(data)


def update(entry, key, values):
    db.child(entry).child(key).update(values)


def delete(entry, key):
    db.child(entry).child(key).remove()


def search_key(entry, attribute, value):
    return search(entry, attribute, value, 'key')


def search_values(entry, attribute, value):
    return search(entry, attribute, value, 'value')


def search(entry, attribute, value, ret):
    data = None
    d = db.child(entry).get().val()
    for u in d:
        data = d[u]
        if data[attribute] == value:
            if ret == 'key':
                data = u
            break
        else:
            data = None
    return data


def search_by_key(entry, key):
    return db.child(entry).child(key).get().val()


if __name__ == '__main__':
    dt = {
        "name": "sera",
        "username": "seraa",
        "email": "sera@sera.com"
        }
    create('users', dt)
    print(search_values('users', 'username', 'juanito'))

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class User:
    def __init__(self, key=None, email=None, username=None, password=None):
        # e.g. __init__(key)
        if key is not None and email is None and username is None and password is None:
            u = db.search_by_key('users', key)
            self.email = u['email']
            self.username = u['username']
            self.password = u['password']
            self.ratings = db.get_dict('ratings', 'user', key)
        # e.g. __init__(email=email, username=username, password=password)
        elif key is None and email is not None and username is not None and password is not None:
            db.create('users', {'email': email, 'username': username, 'password': password})
            self.email = email
            self.username = username
            self.password = password

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_ratings(self):
        r = self.ratings
        if r is None:
            return f'No ratings were found with user : "{self.username}".'
        else:
            return r

    def delete(self, key):
        ratings_list = self.get_ratings()
        for rating in ratings_list:
            # rating_key = db.search_key('ratings', 'leisure', rating['leisure'])
            db.delete('ratings', rating)
        db.delete('users', key)

    @staticmethod
    def get_dict():
        return db.get_dict('users')

    @staticmethod
    def search_by_email(email):
        r = db.get_dict('users', 'email', email)
        if r is None:
            return f'No user has been found with email : "{email}".'
        else:
            return r

    @staticmethod
    def search_by_username(username):
        r = db.get_dict('users', 'username', username)
        if r is None:
            return f'No user has been found with username : "{username}".'
        else:
            return r

    @staticmethod
    def search_by_key(key):
        r = db.search_by_key('users', key)
        if r is None:
            return f'No user has been found with key : "{key}".'
        else:
            return r

    @staticmethod
    def set_email(key, email):
        db.update('users', key, {'email': email})

    @staticmethod
    def set_username(key, username):
        db.update('users', key, {'username': username})

    @staticmethod
    def set_password(key, password):
        db.update('users', key, {'password': password})

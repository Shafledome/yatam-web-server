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
        # e.g. __init__(email=email, username=username, password=password)
        elif key is None and email is not None and username is not None and password is not None:
            db.create('users', {'email': email, 'username': username, 'password': password})
            self.email = email
            self.username = username
            self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        key = db.search_key('users', 'email', self.email)
        db.update('users', key, {'email': email})
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username
        key = db.search_key('users', 'email', self.email)
        db.update('users', key, {'username': username})

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
        key = db.search_key('users', 'email', self.email)
        db.update('users', key, {'password': password})

    def get_ratings(self):
        key = db.search_key('users', 'email', self.email)
        r = db.get_dict('ratings', 'user', key)
        if r is None:
            return f'No ratings were found with user : "{self.username}".'
        else:
            return r

    def delete(self, key):
        ratings_list = self.get_ratings()
        for rating in ratings_list:
            #rating_key = db.search_key('ratings', 'leisure', rating['leisure'])
            db.delete('ratings', rating)
        db.delete('users', key)

    @staticmethod
    def get_dict():
        return db.get_dict('users')

    @staticmethod
    def search_by_email(email):
        r = db.search_values('users', 'email', email)
        if r is None:
            return f'No user has been found with email : "{email}".'
        else:
            return r

    @staticmethod
    def search_by_username(username):
        r = db.search_values('users', 'username', username)
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

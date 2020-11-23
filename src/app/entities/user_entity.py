import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class User:
    def __init__(self, email, username=None, password=None):
        if username is None and password is None:
            u = self.search_by_email(email)
            self.email = u['email']
            self.username = u['username']
            self.password = u['password']
        else:
            db.create('users', {'email': email, 'username': username, 'password': password})
            self.email = email
            self.username = username
            self.password = password

    # Primary key doesn't have set method
    def get_email(self):
        return self.email

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

    @staticmethod
    def get_dict():
        return db.get_dict('users')

    @staticmethod
    def search_by_email(email):
        r = db.search_values('users', 'email', email)
        if r is None:
            return f'No user has been found with email = "{email}".'
        else:
            return r

    @staticmethod
    def search_by_username(username):
        r = db.search_values('users', 'username', username)
        if r is None:
            return f'No user has been found with username = "{username}".'
        else:
            return r
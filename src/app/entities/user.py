import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class User:

    def __init__(self, email, username=None, password=None):
        if username is None and password is None:
            u = db.get('user', email)
            self.email = email
            self.username = u['username']
            self.password = u['password']
        else:
            db.create('user', email, {'username': username, 'password': password})
            self.email = email
            self.username = username
            self.password = password

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username





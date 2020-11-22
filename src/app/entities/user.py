import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class User:

    def __init__(self, email, username=None, password=None):
        if username is None and password is None:
            u = db.get('users', email)
            self.email = email
            self.username = u['username']
            self.password = u['password']
        else:
            db.create('users', email, {'username': username, 'password': password})
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
        db.update('users', self.email, {'username': username})

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
        db.update('users', self.email, {'password': password})

    @staticmethod
    def get_dict():
        return db.get('users')

    @staticmethod
    def search_by_email(email):
        return db.get('users', email)

    def search_by_username(username):
        data = None
        d = db.get('users')
        for u in d:
            data = d[u]
            if data['username'] == username:
                break
            else:
                data = None
        return data






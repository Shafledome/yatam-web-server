import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class Rating:

    def __init__(self, rating_id, user_email=None, leisure_id=None):
        if user_email is None and leisure_id is None:
            r = db.get_dict('rating', rating_id)
            self.id = rating_id
            self.user_email = r['user_email']
            self.leisure_id = r['leisure_id']
        else:
            db.create('rating', {'user_email': user_email, 'leisure_id': leisure_id})
            self.rating_id = rating_id
            self.user_email = user_email
            self.leisure_id = leisure_id

    def get_user_email(self):
        return self.user_email

    def get_leisure_id(self):
        return self.leisure_id

    # Primary key doesn't have set method

    def set_user_email(self, user_email):
        self.user_email = user_email
        key = db.search_key('rating', 'user_email', self.user_email)
        db.update('rating', key, {'user_email': user_email})

    def set_leisure_id(self, leisure_id):
        self.leisure_id = leisure_id
        key = db.search_key('rating', 'leisure_id', self.leisure_id)
        db.update('rating', key, {'leisure_id': leisure_id})

    @staticmethod
    def get_dict():
        return db.get_dict('rating')

    @staticmethod
    def search_by_user(user_email):
        return db.search_values('rating', 'user_email', user_email)

    @staticmethod
    def search_by_leisure(leisure_id):
        return db.search_values('rating', 'leisure_id', leisure_id)

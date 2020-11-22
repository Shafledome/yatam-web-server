import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db

class Rating:

    def __init__(self, rating_id, user_email=None, leisure_id=None):
        if user_email is None and leisure_id is None:
            r = db.get('rating', id)
            self.id = rating_id
            self.user_email = r['user_email']
            self.leisure_id = r['leisure_id']
        else:
            db.create('rating', rating_id, {'user_email': user_email, 'leisure_id': leisure_id})
            self.rating_id = rating_id
            self.user_email = user_email
            self.leisure_id = leisure_id

    def get_rating_id(self):
        return self.rating_id

    def get_user_email(self):
        return self.user_email

    def get_leisure_id(self):
        return self.leisure_id

    # Primary key doesn't have set method

    def set_user_email(self, user_email):
        self.user_email = user_email

    def set_leisure_id(self, leisure_id):
        self.leisure_id = leisure_id

    @staticmethod
    def get_dict():
        return db.get('rating')

    def search_by_user(user_email):
        data = None
        d = db.get('rating')
        for r in d:
            data = d[r]
            if data['user_email'] == user_email:
                break
            else:
                data = None
        return data

    def search_by_leisure(leisure_id):
        data = None
        d = db.get('rating')
        for r in d:
            data = d[r]
            if data['leisure_id'] == leisure_id:
                break
            else:
                data = None
        return data
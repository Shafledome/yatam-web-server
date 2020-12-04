import os
import sys
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class Trophy:
    def __init__(self, key=None, trophy=None, user=None):
        if key is not None and trophy is None and user is None:
            t = db.search_by_key('trophies', key)
            self.trophy = t['trophy']
            self.user = t['user']
            self.date = t['date']
        elif key is None and trophy is not None and user is not None:
            date = datetime.datetime.now().strftime("%c")
            db.create('trophies', {'trophy': trophy, 'user': user, 'date': date})
            self.trophy = trophy
            self.user = user
            self.date = date

    def get_user_key(self):
        return self.user

    def get_trophy_key(self):
        return self.trophy

    def get_date(self):
        return self.date

    @staticmethod
    def delete(key):
        db.delete('trophy', key)

    @staticmethod
    def get_dict():
        return db.get_dict('trophy')

    @staticmethod
    def search_by_key(key):
        return db.search_by_key('trophy', key)

    @staticmethod
    def search_by_user(user):
        return db.get_dict('trophy', 'user', user)

    @staticmethod
    def search_by_trophy(trophy):
        return db.get_dict('trophy', 'trophy', trophy)

    @staticmethod
    def set_user(key, user):
        db.update('trophy', key, {'user': user})

    @staticmethod
    def set_trophy(key, trophy):
        db.update('trophy', key, {'trophy': trophy})

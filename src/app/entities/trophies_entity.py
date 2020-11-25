import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class TrophyList:
    def __init__(self, key=None, name=None, text=None):
        if key is not None and name is None and text is None:
            t = db.search_by_key('trophies', key)
            self.name = t['name']
            self.text = t['text']
        elif key is None and name is not None and text is not None:
            db.create('trophies', {'name': name, 'text': text})
            self.name = name
            self.text = text

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    @staticmethod
    def delete(key):
        db.delete('trophies', key)

    @staticmethod
    def get_dict():
        return db.get_dict('trophies')

    @staticmethod
    def search_by_trophy_key(key):
        return db.search_by_key('trophies', key)

    @staticmethod
    def search_by_name(name):
        return db.search_values('trophies', 'name', name)

    @staticmethod
    def set_name(key, name):
        db.update('trophies', key, {'name': name})

    @staticmethod
    def set_text(key, text):
        db.update('trophies', key, {'text': text})
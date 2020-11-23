import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class TrophyList:
    def __init__(self, trophy_id, name=None, text=None):
        if name is None and text is None:
            t = db.search_by_key('trophies', trophy_id)
            self.trophy_id = t['trophy_id']
            self.name = t['name']
            self.text = t['text']
        else:
            db.create('trophies', {'name': name, 'text': text})
            self.trophy_id = trophy_id
            self.name = name
            self.text = text

    def get_trophy_id(self):
        return self.trophy_id

    # Primary key has no setter

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        key = db.search_key('trophies', 'name', self.trophy_id)
        db.update('trophies', key, {'name': name})

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text
        key = db.search_key('trophies', 'text', self.trophy_id)
        db.update('trophies', key, {'text': text})

    @staticmethod
    def get_dict(trophy_id):
        return db.get_dict('trophies', trophy_id)

    @staticmethod
    def search_by_trophy_id(trophy_id):
        return db.search_by_key('trophies', trophy_id)

    @staticmethod
    def search_by_name(name):
        return db.search_values('trophies', 'name', name)

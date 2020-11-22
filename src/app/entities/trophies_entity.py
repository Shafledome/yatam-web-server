import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class TrophyList:

    def __init__(self, trophy_id, name=None, text=None):
        if name is None and text is None:
            t = db.get('trophies', trophy_id)
            self.trophy_id = trophy_id
            self.name = t['name']
            self.text = t['text']
        else:
            db.create('trophies', trophy_id, {'name': name; 'text': text})
            self.trophy_id = trophy_id
            self.name = name
            self.text = text

    def get_trophy_id(self):
        return self.trophy_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name=name
        db.update('trophies', self.trophy_id, {'name': name})

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text=text
        db.update('trophies', self.trophy_id, {'text': text})

    @staticmethod
    def get_dict():
        return db.get('trophies', trophy_id)

    @staticmethod
    def search_by_trophy_id(trophy_id):
        return db.get('trophies', trophy_id)

    def search_by_name(name):
            data = None
            d = db.get('trophies')
            for t in d:
                data = d[t]
                if data['name'] == name:
                    break
                else:
                    data = None
            return data

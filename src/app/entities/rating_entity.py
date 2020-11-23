import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class Rating:

    def __init__(self, rating_id=None, user=None, leisure=None, grade=None, text=None):
        if user is None and leisure is None and grade is None and text is None:
            r = db.get_dict('ratings', rating_id)
            self.user = r['user']
            self.leisure = r['leisure']
            self.grade = r['grade']
            self.text = r['text']
        else:
            db.create('ratings', {'user': user, 'leisure': leisure, 'grade': grade, 'text': text})
            self.user = user
            self.leisure = leisure
            self.grade = grade
            self.text = text

    def get_user(self):
        return self.user

    def get_leisure(self):
        return self.leisure

    def get_grade(self):
        return self.grade

    def get_text(self):
        return self.text

    # Primary keys don't have set method

    def set_grade(self, grade):
        self.grade = grade
        key = db.search_key('ratings', 'grade', self.grade)
        db.update('ratings', key, {'grade': grade})

    def set_text(self, text):
        self.text = text
        key = db.search_key('ratings', 'text', self.text)
        db.update('ratings', key, {'text': text})

    @staticmethod
    def get_dict():
        return db.get_dict('ratings')

    @staticmethod
    def search_by_user(user):
        return db.search_values('ratings', 'user', user)

    @staticmethod
    def search_by_leisure(leisure):
        return db.search_values('ratings', 'leisure', leisure)

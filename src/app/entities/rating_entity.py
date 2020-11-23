import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class Rating:

    def __init__(self, rating_id=None, user=None, leisure=None, grade=None, text=None):
        if user is None and leisure is None and grade is None and text is None:
            r = db.search_by_key('ratings', rating_id)
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

    # Primary keys don't have setter

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
        r = db.search_values('ratings', 'user', user)
        if r is not None:
            return r
        else:
            return f'No rating has been found with user id : "{user}".'

    @staticmethod
    def search_by_leisure(leisure):
        r = db.search_values('ratings', 'leisure', leisure)
        if r is not None:
            return r
        else:
            return f'No rating has been found with leisure id : "{leisure}".'

    @staticmethod
    def search_by_user_and_leisure(user, leisure):
        data = None
        d = db.search_values('ratings', 'user', user)
        for r in d:
            data = d[r]
            if data['leisure'] == leisure:
                break
            else:
                data = None
        if data is not None:
            return data
        else:
            return f'No rating has been found with user id : "{user}" and leisure id : "{leisure}".'

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class Rating:

    def __init__(self, key=None, user=None, leisure=None, grade=None, text=None):
        if key is not None and user is None and leisure is None and grade is None and text is None:
            # e.g. __init__(key)
            r = db.search_by_key('ratings', key)
            self.user = r['user']
            self.leisure = r['leisure']
            self.grade = r['grade']
            self.text = r['text']
        elif key is None and user is not None and leisure is not None and grade is not None and text is not None:
            # e.g. __init__(user, leisure, grade, text)
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

    # Primary keys (user and leisure) don't have setter

    @staticmethod
    def delete(key):
        db.delete('ratings', key)

    @staticmethod
    def get_dict():
        return db.get_dict('ratings')

    @staticmethod
    def search_by_id(key):
        r = db.search_by_key('ratings', key)
        if r is not None:
            return r
        else:
            return f'No rating has been found with rating id : "{key}".'

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
        d = db.get_dict('ratings', 'user', user)
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

    @staticmethod
    def set_grade(key, grade):
        db.update('ratings', key, {'grade': grade})

    @staticmethod
    def set_text(key, text):
        db.update('ratings', key, {'text': text})

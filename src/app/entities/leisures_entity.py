import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.opendata as opendata

'''
We have different types of leisures. Museum, art gallery, dog park, monuments, training, library, cinema and
theater. To ask it to the opendata.py file, we will ask it in UPPERCASE and without white spaces.
'''


class LeisureList:
    def __init__(self, leisure_type: str):
        self.leisures = opendata.parse_json_data(leisure_type)

    def get_by_id(self, leisure_id: int):
        return self.leisures.get(leisure_id)


if __name__ == '__main__':
    museum_list = LeisureList('MUSEUM')
    print(museum_list.get_by_id(710))

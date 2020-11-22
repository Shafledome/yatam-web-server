import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.opendata as opendata

'''
We have different types of leisures. Museum, art gallery, dog park, monuments, training, library, cinema and
theater. To ask it to the opendata.py file, we will ask it in UPPERCASE and without white spaces.
'''

# dictionary entry:
entry = 'MUSEUM'

all_data = opendata.parse_json_data('MUSEUM')


def get_all_data():
    return all_data


def get_museum_by_id(museum_id: int = None):
    if museum_id is None:
        raise ValueError('Id is None.')
    else:
        return all_data[museum_id]


if __name__ == '__main__':
    print(get_museum_by_id(710))

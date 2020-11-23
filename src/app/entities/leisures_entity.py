import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.opendata as opendata

'''
We have different types of leisures. Museum, art gallery, dog park, monuments, training, library, cinema and
theater. To ask it to the opendata.py file, we will ask it in UPPERCASE and without white spaces.
'''


class LeisureList:
    def __init__(self, leisure_type: str):
        self.leisure_type = leisure_type
        self.leisures = opendata.parse_json_data(leisure_type)

    def get_all(self):
        return self.leisures

    def get_by_id(self, leisure_id: int):
        if isinstance(leisure_id, int):
            return self.leisures.get(leisure_id)
        else:
            return leisure_id

    def get_id_by_name(self, leisure_name: str):
        for l_id in self.leisures:
            if self.leisures.get(l_id)['name'] == leisure_name:
                return l_id
        return f'"{leisure_name}" not found in {self.leisure_type.lower()}s.'

    def get_id_by_coordinates(self, latitude: float, longitude: float):
        for l_id in self.leisures:
            if self.leisures.get(l_id)['coordinates'] == [latitude, longitude]:
                return l_id
        return f'A {self.leisure_type.lower()} with the coordinates: {latitude, longitude} has not been found.'

    def get_id_by_address(self, address: str):
        for l_id in self.leisures:
            if self.leisures.get(l_id)['address'] == address:
                return l_id
        return f'A {self.leisure_type.lower()} with the address: "{address}" has not been found.'

    def get_id_by_url(self, url: str):
        for l_id in self.leisures:
            if self.leisures.get(l_id)['url'] == url:
                return l_id
        return f'A {self.leisure_type.lower()} with the URL: "{url}" has not been found.'


if __name__ == '__main__':
    museum_list = LeisureList('MUSEUM')
    print(museum_list.get_by_id(710))
    print(museum_list.get_id_by_name('Auditorio Castillo de Gibralfaro'))
    print(museum_list.get_id_by_coordinates(36.7233413, -4.41014619))
    print(museum_list.get_id_by_address('CAMINO GIBRALFARO, 11 '))
    print(museum_list.get_id_by_url('http://www.malaga.euÂ\xa0'))
    print(museum_list.get_all())

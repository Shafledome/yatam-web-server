import requests

museumJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_museos-4326.geojson'
artGalleryJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_galeriasArte-4326.geojson'
dogParkJSON = 'https://datosabiertos.malaga.eu/recursos/ambiente/parquesCaninos/da_parquesCaninos-4326.geojson'
monumentsJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_monumentos-4326.geojson'
trainingParkJSON = 'https://datosabiertos.malaga.eu/recursos/deportes/equipamientos/da_deportesZonasMusculacion-4326.geojson'
bikePointJSON = 'https://datosabiertos.malaga.eu/recursos/transporte/EMT/EMTocupestacbici/ocupestacbicifiware.json'
libraryJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_bibliotecas-4326.geojson'
cinemaJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_cines-4326.geojson'
theaterJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_teatros-4326.geojson'


def download_open_data(url):
    response = requests.get(url)

    if response.status_code >= 400:
        raise RuntimeError(f'Error with request. Code: {response.status_code}')

    return response.json()


def parse_json_data(leisure_type: str):
    switcher = {
        'MUSEUM': museumJSON,
        'ARTGALLERY': artGalleryJSON,
        'DOGPARK': dogParkJSON,
        'MONUMENTS': monumentsJSON,
        'TRAINING': trainingParkJSON,
        'LIBRARY': libraryJSON,
        'CINEMA': cinemaJSON,
        'THEATER': theaterJSON
    }
    json_url = switcher.get(leisure_type, lambda: 'Invalid type')

    data = download_open_data(json_url)
    features = data['features']
    result = {}

    for feature in features:
        longitude = feature['geometry']['coordinates'][0]
        latitude = feature['geometry']['coordinates'][1]
        coordinates = {'coordinates': [latitude, longitude]}
        id_leisure = feature['properties']['ID']
        name = feature['properties']['NOMBRE']
        description = feature['properties']['DESCRIPCION']
        address = feature['properties']['DIRECCION']
        url = feature['properties']['URL']
        email = feature['properties']['EMAIL']
        schedule = feature['properties']['HORARIOS']
        data = {'name': name, 'description': description, 'address': address, 'url': url, 'email': email, 'schedule': schedule}
        result[id_leisure] = data

    return result


if __name__ == '__main__':
    print(parse_json_data('DOGPARK'))

import requests

museumJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_museos-4326.geojson'
artGalleryJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_galeriasArte-4326.geojson'
dogParkJSON = 'https://datosabiertos.malaga.eu/recursos/ambiente/parquesCaninos/da_parquesCaninos-4326.geojson'
monumentJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_monumentos-4326.geojson'
trainingParkJSON = 'https://datosabiertos.malaga.eu/recursos/deportes/equipamientos/da_deportesZonasMusculacion-4326.geojson'
libraryJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_bibliotecas-4326.geojson'
cinemaJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_cines-4326.geojson'
theaterJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_teatros-4326.geojson'

trafficCutsJSON = 'https://datosabiertos.malaga.eu/recursos/transporte/trafico/da_cortesTrafico-4326.geojson'


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
        'MONUMENT': monumentJSON,
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
        id_leisure = feature['properties']['ID']
        name = feature['properties']['NOMBRE']
        description = feature['properties']['DESCRIPCION']
        address = feature['properties']['DIRECCION']
        url = feature['properties']['URL']
        email = feature['properties']['EMAIL']
        schedule = feature['properties']['HORARIOS']
        data = {'id': id_leisure, 'name': name, 'description': description, 'address': address, 'url': url, 'email': email, 'schedule': schedule, 'coordinates': [latitude, longitude]}
        result[id_leisure] = data

    return result


def parse_traffic_json_data():
    data = download_open_data(trafficCutsJSON)
    features = data['features']
    result = {}

    for feature in features:
        longitude = feature['geometry']['coordinates'][0]
        latitude = feature['geometry']['coordinates'][1]
        id_traffic = feature['properties']['ogc_fid']
        name = feature['properties']['name']
        description = feature['properties']['description']
        data = {'name': name, 'description': description, 'coordinates': [latitude, longitude]}
        result[id_traffic] = data
    return result


if __name__ == '__main__':
    print(parse_json_data('DOGPARK'))
    print(parse_traffic_json_data())

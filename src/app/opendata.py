import requests

museumJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_museos-4326.geojson'
artGalleryJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_galeriasArte-4326.geojson'
dogParkJSON = 'https://datosabiertos.malaga.eu/recursos/ambiente/parquesCaninos/da_parquesCaninos-4326.geojson'
monumentsJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_monumentos-4326.geojson'
trainingParkJSON = 'https://datosabiertos.malaga.eu/recursos/deportes/equipamientos/da_deportesZonasMusculacion-4326.geojson'
bikePointJSON = 'https://datosabiertos.malaga.eu/recursos/transporte/EMT/EMTocupestacbici/ocupestacbicifiware.json'
libraryJSON = 'https://datosabiertos.malaga.eu/recursos/urbanismoEInfraestructura/equipamientos/da_cultura_ocio_bibliotecas-4326.geojson'


def download_open_data(url):
    response = requests.get(url)

    if response.status_code >= 400:
        raise RuntimeError(f'Error with request. Code: {response.status_code}')

    return response.json()


def get_all_museum_data():
    data = download_open_data(museumJSON)
    features = data['features']
    result = {}

    for feature in features:
        longitude = feature['geometry']['coordinates'][0]
        latitude = feature['geometry']['coordinates'][1]
        coordinates = {'coordinates': [latitude, longitude]}
        id_museum = features['properties']['ID']
        name = features['properties']['NOMBRE']
        description = features['properties']['DESCRIPCION']
        address = features['properties']['DIRECCION']
        url = features['properties']['URL']
        email = features['properties']['EMAIL']
        schedule = features['properties']['HORARIOS']
        result[id_museum] = (name, description, address, coordinates, email, url, schedule)


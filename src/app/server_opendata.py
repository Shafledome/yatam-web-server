from flask import Flask, Response, json
from flask_cors import CORS
from entities.leisures_entity import LeisureList
from entities.events_entity import EventsList


'''
Information about CORS:
https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
Basically, AJAX (Asynchronous Javascript And XML) is a type of CORS 
'''

app = Flask(__name__)
CORS(app)

# flask default method: GET
# mime type for json files
# https://www.ietf.org/rfc/rfc4627.txt
# https://stackoverflow.com/questions/477816/what-is-the-correct-json-content-type
# status if servers returns the requested info is 200
mimetype = 'application/json'

leisures_type = [
    'MUSEUM',
    'ARTGALLERY',
    'DOGPARK',
    'MONUMENT',
    'TRAINING',
    'LIBRARY',
    'CINEMA',
    'THEATER'
]


# Returns JSON with all leisures
@app.route('/leisures/all')
def get_all_leisures():
    result = {}
    for leisure_type in leisures_type:
        leisures = LeisureList(leisure_type.upper()).get_all()
        result = {** result, **leisures}
    status = 200
    if not isinstance(result, dict):
        status = 500
        if result is None:
            result = {'error': f'Error 500. Internal server error.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with all leisures of a type
@app.route('/leisures/<string:leisure_type>')
def get_leisures_by_type(leisure_type):
    result = LeisureList(leisure_type.upper()).get_all()
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. Type: {leisure_type} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a leisure by its type and name
@app.route('/leisures/<string:leisure_type>/name/<string:leisure_name>')
def get_leisure_by_type_and_name(leisure_type, leisure_name):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_name(leisure_name))
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. ID: {leisure_name} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a leisure by its type and id
@app.route('/leisures/<string:leisure_type>/id/<int:leisure_id>')
def get_leisure_by_type_and_id(leisure_type, leisure_id):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisure_id)
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. ID: {leisure_id} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a leisure by its type and address
@app.route('/leisures/<string:leisure_type>/address/<string:leisure_address>')
def get_leisure_by_type_and_address(leisure_type, leisure_address):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_address(leisure_address))
    status = 200
    if not isinstance(result, dict):
        status = 404
        result = {'error': result}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a leisure by its type and url
@app.route('/leisures/<string:leisure_type>/url/<string:leisure_url>')
def get_leisure_by_type_and_url(leisure_type, leisure_url):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_url(leisure_url))
    status = 200
    if not isinstance(result, dict):
        status = 404
        result = {'error': result}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a leisure by its type and coordinates
@app.route('/leisures/<string:leisure_type>/latitude/<string:latitude>/longitude/<string:longitude>')
def get_leisure_by_type_and_coordinates(leisure_type, latitude, longitude):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_coordinates(float(latitude), float(longitude)))
    status = 200
    if not isinstance(result, dict):
        status = 404
        result = {'error': result}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about an event by its activity ID
@app.route('/events/activity_id/<string:activity_id>')
def get_events_by_activity_id(activity_id):
    events = EventsList()
    result = events.get_by_activity_id(activity_id)
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. ID: {activity_id} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about an event by its name
@app.route('/events/name/<string:events_name>')
def get_events_by_name(events_name):
    events = EventsList()
    result = events.get_by_activity_id(events.get_id_by_name(events_name))
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. Event with name: {events_name} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about an event by its event ID
@app.route('/events/event_id/<string:events_id>')
def get_events_by_events_id(events_id):
    events = EventsList()
    result = events.get_by_activity_id(events.get_id_by_event_id(events_id))
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. Event with name: {events_id} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about an event by its location id
@app.route('/events/location/<string:location_id>')
def get_events_by_location_id(location_id):
    events = EventsList()
    result = events.get_by_activity_id(events.get_id_by_location_id(location_id))
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. Event with name: {location_id} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about an event by its category
@app.route('/events/category/<string:category>')
def get_events_by_category(category):
    events = EventsList()
    result = events.get_by_activity_id(events.get_id_by_category(category))
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404. Event with name: {category} was not found.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/events/all')
def get_all():
    events = EventsList()
    result = events.get_all()
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = {'error': f'Error 404'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=30006, debug=True)

from flask import Flask, request, Response, jsonify, json
from flask_cors import CORS, cross_origin
from entities.leisures_entity import LeisureList
from entities.traffic_cuts_entity import TrafficList


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


# Returns JSON with data about a leisure by its type and name
@app.route('/leisures/<string:leisure_type>/name/<string:leisure_name>')
def get_leisure_by_type_and_name(leisure_type, leisure_name):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_name(leisure_name))
    status = 200
    if not isinstance(result, dict):
        status = 404
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
            result = f'Error 404. ID: {leisure_id} was not found.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a leisure by its type and address
@app.route('/leisures/<string:leisure_type>/address/<string:leisure_address>')
def get_leisure_by_type_and_address(leisure_type, leisure_address):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_address(leisure_address))
    status = 200
    if not isinstance(result, dict):
        status = 404
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a leisure by its type and url
@app.route('/leisures/<string:leisure_type>/url/<string:leisure_url>')
def get_leisure_by_type_and_url(leisure_type, leisure_url):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_url(leisure_url))
    status = 200
    if not isinstance(result, dict):
        status = 404
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a traffic cut by its name
@app.route('/traffic_cuts/name/<int:traffic_cuts_name>')
def get_traffic_cuts_by_name(traffic_cuts_name):
    traffic_cuts = TrafficList()
    result = traffic_cuts.get_by_id(traffic_cuts.get_id_by_name(traffic_cuts_name))
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = f'Error 404. ID: {traffic_cuts_name} was not found.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# Returns JSON with data about a traffic cut by its id
@app.route('/traffic_cuts/id/<int:traffic_cuts_id>')
def get_traffic_cuts_by_id(traffic_cuts_id):
    traffic_cuts = TrafficList()
    result = traffic_cuts.get_by_id(traffic_cuts_id)
    status = 200
    if not isinstance(result, dict):
        status = 404
        if result is None:
            result = f'Error 404. ID: {traffic_cuts_id} was not found.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=30006, debug=True)

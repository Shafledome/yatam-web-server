from flask import Flask, request, Response, jsonify, json
from flask_cors import CORS, cross_origin

'''
Information about CORS:
https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
Basically, AJAX (Asynchronous Javascript And XML) is a type of CORS 
'''

app = Flask(__name__)
CORS(app)

# flask default method: GET
# metadata headers: content-type: application/json
headers = {'content-type': 'application/json'}

# Returns JSON with data about a leisure by it's type and name
@app.route('/leisures/<string: leisure_type>/<string: leisure_name>')
def get_leisure_by_type_and_name(leisure_type, leisure_name):
    try:
        # ToDo: Petition Entity parsed data
    except ValueError:
        return Response(json.dumps(
            f'Error 404. Leisure {leisure_name} with type {leisure_type} not found.',
            headers= headers,
            status= 200))
    # ToDo: Return Response with data and status
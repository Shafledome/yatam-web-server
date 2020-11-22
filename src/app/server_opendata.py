from flask import Flask, request, Response, jsonify, json
from flask_cors import CORS, cross_origin
from entities.leisures_entity import LeisureList


'''
Information about CORS:
https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
Basically, AJAX (Asynchronous Javascript And XML) is a type of CORS 
'''

app = Flask(__name__)
CORS(app)

# flask default method: GET
# metadata headers = content-type: application/json
# https://www.ietf.org/rfc/rfc4627.txt
# https://stackoverflow.com/questions/477816/what-is-the-correct-json-content-type
mimetype = 'application/json'


# Returns JSON with data about a leisure by it's type and name
@app.route('/leisures/<string:leisure_type>/<string:leisure_name>')
def get_leisure_by_type_and_name(leisure_type, leisure_name):
    leisures = LeisureList(leisure_type.upper())
    result = leisures.get_by_id(leisures.get_id_by_name(leisure_name))
    return Response(json.dumps(result), mimetype=mimetype, status=200)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=30006, debug=True)

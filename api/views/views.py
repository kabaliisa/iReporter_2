from flask import jsonify,request
from api import app
from api.models.redflags import Incident,redflags



@app.route('/api/v1/redflags', methods=['GET'])
def get_all_redflags():
    reds = []
    for redflag in redflags:
        reds.append(redflag.to_json())

    if len(reds) < 1:
        return jsonify({'status':404,'message': 'There are no red-flags'}),404
    return jsonify({'status':201,'data': reds}),201
from flask import jsonify,request
from api import app
from api.models.redflags import Incident,redflags


@app.route('/api/v1/redflags/<int:id>', methods=['GET'])
def get_specific_redflags(id):
    for redflag in redflags:  
        if redflag.to_json()['id']== id:
            return jsonify({'status':201,'data':redflag.to_json()}),201
       
    return jsonify({'status':404 ,'message': 'Red-flag not found'}),404 
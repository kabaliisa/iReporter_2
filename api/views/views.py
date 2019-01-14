from flask import jsonify,request
from api import app
from api.models.redflags import Incident,redflags

@app.route('/api/v1/redflags/<int:id>', methods=['DELETE'])
def remove_specific_redflag(id):
    for redflag in redflags:
        if redflag.to_json()['id']== id:
            redflags.remove(red-flag)
        else:
            return jsonify({'status':404,'message':'not found'}),404    
    return jsonify({'status':200 ,'id':red-flag.to_json()['id'],'message': 'red-flag record has been deleted'}),200


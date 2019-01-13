from flask import jsonify,request
from api import app
from api.models.redflags import Incident,redflags

@app.route('/api/v1/redflags/<int:id>/location', methods=['PATCH'])
def edit_specific_location(id):
   
    get_new_location = request.get_json()
    
    for redflag in redflags:
        if redflag.to_json()['id']== id:
            redflag.to_json()['location'] = get_new_location['location']      
            return jsonify({'status':200,'id':redflag.to_json()['id'],'message':"Updated red-flag record's location"})       
    return jsonify({'status':404 ,'message': 'Red-flag not found'}) 
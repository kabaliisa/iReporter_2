from flask import jsonify,request
from api import app
from api.models.redflags import Incident,redflags


@app.route('/api/v1/redflags', methods=['POST'])
def add_redflag():
    data = request.get_json()
    

    latitude = data['latitude']
    longitude = data['longitude']
    
    image = data['image']
   

    location = {
        "latitude": latitude,
        "longitude": longitude
    }

    try:
        if type(data['createdBy']) is not str:
            raise ValueError('This  should be a string')
    
        redflag = Incident(id, 'createdOn', data['createdBy'],data['incidentType'], location, data['comment'],image)
        redflags.append(redflag)

    except ValueError:
        
        return jsonify({'status':400,'message': 'createdBy should be a string'}), 400

    return jsonify({'status':201,'data': [redflag.to_json()],'message':'Created red-flag record'}),201



@app.route('/api/v1/redflags', methods=['GET'])
def get_all_redflags():
    reds = []
    for redflag in redflags:
        reds.append(redflag.to_json())

    if len(reds) < 1:
        return jsonify({'status':404,'message': 'There are no red-flags'}),404
    return jsonify({'status':201,'data': reds}),201


@app.route('/api/v1/redflags/<int:id>', methods=['GET'])
def get_specific_redflags(id):
    for redflag in redflags:  
        if redflag.to_json()['id']== id:
            return jsonify({'status':201,'data':redflag.to_json()}),201
       
    return jsonify({'status':404 ,'message': 'Red-flag not found'}),404 

@app.route('/api/v1/redflags/<int:id>/location', methods=['PATCH'])
def edit_specific_location(id):
    get_new_location = request.get_json()
    
    for redflag in redflags:
        if redflag.to_json()['id']== id:
            redflag.to_json()['location'] = get_new_location['location']      
            return jsonify({'status':200,'id':redflag.to_json()['id'],'message':"Updated red-flag record's location"})       
    return jsonify({'status':404 ,'message': 'Red-flag not found'}),404 

@app.route('/api/v1/redflags/<int:id>', methods=['DELETE'])
def remove_specific_redflag(id):
    for redflag in redflags:
        if redflag.to_json()['id']== id:
            redflags.remove(red-flag)
        else:
            return jsonify({'status':404,'message':'not found'}),404    
    return jsonify({'status':200 ,'id':red-flag.to_json()['id'],'message': 'red-flag record has been deleted'}),200

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

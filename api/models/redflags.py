import datetime

redflags = []

class Incident:
    def __init__(self,id, createdOn, createdBy, incidentType, location, comment,image):
        self.id = len(redflags)+1
        self.createdBy = createdBy
        self.createdOn = datetime.datetime.now()
        self.incidentType = incidentType
        self.location = location
        self.comment = comment
        self.image = image
        
        

    def to_json(self):
        return {'id': self.id, 'createdOn': self.createdOn, 'createdBy': self.createdBy, 'incidentType':self.incidentType, 'location':self.location, 'comment':self.comment,'image':self.image}
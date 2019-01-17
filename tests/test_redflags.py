import unittest
import json
from api import app
from api.views import views
from api.models.redflags import Incident


class TestRedflag(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_add_redflag(self):
        """Tests add_redflag method"""

        input_data = {
            'createdBy': 'solo',
            'incidentType': 'nepotism',
            'latitude': '6336377',
            'longitude': '676778',
            'image': [
                "fyf",
                "hhshs"],
            'comment': 'gdihdiududh',
            'image': [
                'duck.jpg',
                'ffggg']}
        response = self.app_tester.post('/api/v1/redflags', json=input_data)
        self.assertEqual(response.status_code, 201)

    def test_model_function(self):
        """Tests if dummy data provided is instance of class Incident"""

        self.redflag = Incident(
            id=1,
            createdOn="1/jan/2018",
            createdBy="solo",
            incidentType="bribe",
            location="kla",
            comment="mmnnucuud",
            image="sd.jpg")
        self.assertIsInstance(self.redflag, Incident)

    def test_get_all_redflags(self):
        """Test get_all_redflags method"""

        response = self.app_tester.get("/api/v1/redflags")
        self.assertEqual(response.status_code, 200)

    def test_get_specific_redflags(self):
        """Test get_specific_redflags method"""

        response = self.app_tester.get("/api/v1/redflags/1")
        self.assertEqual(response.status_code, 200)

    def test_remove_specific_redflag(self):
        """Test remove_specific_redflag method"""

        response = self.app_tester.delete("/api/v1/redflags/1")
        self.assertEqual(response.status_code, 200)

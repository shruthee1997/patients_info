from application import app

from flask_testing import TestCase
import unittest


class APITestCase(TestCase):

    def create_app(self):
        # Create an instance of Flask application
        apps = app
        return apps

    def test_get_patient(self):
        response = self.client.get('/patients/1')
        self.assert200(response)
        data = response.json
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'Aaron697')

    def test_post_patient(self):
        data = {
            'name': 'Jane Smith',
            'dob': "1968-07-07",
            'gender': "male",
            'mobile': "123456789"
        }
        response = self.client.post('/patients', json=data)
        self.assertStatus(response, 201)
    
    def test_put_patient(self):
        data = {
            'name': 'Jane Smith',
            'dob': "1968-07-07",
            'gender': "male",
            'mobile': "123456789"
        }
        response = self.client.put('/patients/96', json=data)
        self.assert200(response)
        data = response.json
        self.assertEqual(data['dob'], "1968-07-07")
    
    def test_delete_patient(self):
        response = self.client.delete('/patients/96')
        self.assertStatus(response, 204)


if __name__ == '__main__':
    unittest.main()

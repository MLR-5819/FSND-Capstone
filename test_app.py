import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Entry, Category

user_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtoX3drdVlWNGwzT1FIX2pvaGZ6MSJ9.eyJpc3MiOiJodHRwczovL2Rldi1tcm9zZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3MGQxZjBhNTExZmUwMDZiNzhmZDQwIiwiYXVkIjoidG90IiwiaWF0IjoxNjAxMjU0NTc0LCJleHAiOjE2MDEyNjE3NzQsImF6cCI6ImtZV0JvdjV0eWlZazkwRTZvc0dXaHRGNUlLeENmS3pOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDplbnRyeSIsInBvc3Q6ZW50cnkiXX0.VKeXZrDQ8rZsmDkJUhaEqR7F1ETBrvbbp_9EUvtR7q3OQJptgSrLzwzSGVeDrgSAYOPI0Esw3qiIkw-0UaVNYBwV2J1l2L2I5AMp2imfMc0E8KPJa3YxCWKV8Ji8-GOGdngyQm-Cv4LwKR4GZiCTbQocISNLuwzN8EjhtylKJkE_6hwu2eMecMxB3rMxXrPMUpyq_IpEDdxu2UKOrKfRrLWvdkgxdR5Z9T0gO55DSTWCYnTbemdQnQfCgIxBZBbhZNGBeF_5o8T21cdyR2c1yXb0bx22YoHxSr5B_wNuIvsk2UgPCCQvYjM6Q5tC7_adubTBZGHc7K8wCJUJc3A0LQ'
admin_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtoX3drdVlWNGwzT1FIX2pvaGZ6MSJ9.eyJpc3MiOiJodHRwczovL2Rldi1tcm9zZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3MGQyYWI2MzAwMjQwMDcxOTM4ZmY1IiwiYXVkIjoidG90IiwiaWF0IjoxNjAxMjU0NDk5LCJleHAiOjE2MDEyNjE2OTksImF6cCI6ImtZV0JvdjV0eWlZazkwRTZvc0dXaHRGNUlLeENmS3pOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZW50cnkiLCJwYXRjaDplbnRyeSIsInBvc3Q6ZW50cnkiXX0.QMXDam7eiZlmaWpKyT6HZVgq9EXVR3mLmxF_xutmvikG6b8DJg_3_yHqamrLsBYsZel2PQlwG8WgXkXh3z5NkzrPyp2EvJ1dYWqK3ZSVzpKo5dv7A-16oxci30UR_1gpOCDTLUYhkCVtuxIvrWi33G7xIIMmB-0aJSujWynni_ojGO_4WPvl2XDsTG6We9yy8RP8KcOyqhUdJ6-Bgt5p-NFmuEq1epk063aPRZzgRf8tzwXu-Xu1AjOXqeKtVCRaCoDwSZ6KTUXyy41ETvoosiSWKcl8CdIRl_dgcHEAVA99gWrNdzc3YfSC7DRtVcKBdrCX7OPwp0Ya7PkPLbt3BQ'


class ThisOrThatTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "thisorthat"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'password', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        #Executed after reach test
        pass

    def test_index(self):
        result = self.client().get('/')

        self.assertEqual(result.status_code, 200)

    def test_get_categories(self):
        result = self.client().get('/api/categories')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['entries'])

    def test_show_categories(self):
        result = self.client().get('/api/categories/1')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['entries'])

    def test_404_no_show_categories(self):
        result = self.client().get('/api/categories/0')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_show_entry(self):
        result = self.client().get('/api/entries/1')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['entry'])

    def test_404_no_show_entry(self):
        result = self.client().get('/api/entries/100000')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_get_add_entry(self):
        result = self.client().get('/api/categories')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['entries'])

    def test_post_add_entry(self):
        new_entry = {
            'name': 'test entry',
            'category': 1,
            'url': 'www.google.com'
        }

        result = self.client().post('/api/entries/add', json=new_entry)
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_failed_add_entry(self):
        result = self.client().post('/api/entries/add',
                                    data=dict(name='test no url',
                                              category='1',
                                              url=''))
        data = result.get_json()

        self.assertEqual(result.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_get_update_entry(self):
        result = self.client().get(
            '/api/entries/1/update',
            headers={'Authorization': 'Bearer ' + user_jwt})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['category'])
        self.assertTrue(data['entry'])

    def test_401_patch_not_auth_update_entry(self):
        patch_entry = {'id': 46, 'name': 'updated test entry', 'category': 2}

        result = self.client().patch('/api/entries/46/update',
                                     json=patch_entry)
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_update_entry(self):
        #update API endpoint ID to match your database
        patch_entry = {'id': 46, 'name': 'updated test entry', 'category': 2}

        #User level authorization
        result = self.client().patch(
            '/api/entries/46/update',
            json=patch_entry,
            headers={'Authorization': 'Bearer ' + user_jwt})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_failed_no_update_entry(self):
        patch_entry = {
            'id': 100000,
            'name': 'updated test entry',
            'category': 2
        }
        #User level auth
        result = self.client().patch(
            '/api/entries/100000/update',
            json=patch_entry,
            headers={'Authorization': 'Bearer ' + user_jwt})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_400_failed_update_entry(self):
        #update API endpoint ID to match your database
        result = self.client().patch(
            '/api/entries/49/update',
            data=dict(name='test no category', category=''),
            headers={'Authorization': 'Bearer ' + user_jwt})
        data = result.get_json()

        self.assertEqual(result.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_delete_entry(self):
        #update API endpoint ID to match your database
        #Admin level auth
        result = self.client().delete(
            '/api/entries/51/delete',
            headers={'Authorization': 'Bearer ' + admin_jwt})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_not_auth_delete_entry(self):
        #update API endpoint ID to match your database
        #user level auth, not authorized to delete
        result = self.client().delete(
            '/api/entries/51/delete',
            headers={'Authorization': 'Bearer ' + user_jwt})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_failed_delete_no_entry(self):
        result = self.client().delete(
            '/api/entries/100000/delete',
            headers={'Authorization': 'Bearer ' + admin_jwt})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

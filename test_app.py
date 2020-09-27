import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Entry, Category

class ThisOrThatTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "thisorthat"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','password','localhost:5432', self.database_name)
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

    def test_422_failed_add_entry(self):
    
    def test_update_entry(self):

    def test_404_failed_no_update_entry(self):

    def test_422_failed_update_entry(self):

    def test_delete_entry(self):
    
    def test_404_failed_delete_no_entry(self):

    def test_422_failed_delete_entry(self):

    #400 error
    #405 error
    #500 error

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

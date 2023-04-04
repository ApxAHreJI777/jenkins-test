import unittest
import os
import json

# os.environ['SECRET_KEY'] = 'test_secret'
# os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test_shopping_list'

from app import app

class BaseCase(unittest.TestCase):
    login_ednpoint = '/api/v1/login'

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

import unittest

from tests.BaseCase import BaseCase

class TestIndex(BaseCase):
    def test_index(self):
        response = self.client.get('/', headers={"Content-Type": "application/json"})

        self.assertEqual(200, response.status_code)

    def test_404(self):
        response = self.client.get('/invalid-index-url-test-404', headers={"Content-Type": "application/json"})

        self.assertEqual(404, response.status_code)
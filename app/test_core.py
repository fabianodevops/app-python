from app import app_code

import unittest

class TestHomeView(unittest.TestCase): 

    def setUp(self):
        app = app_code.test_client()
        self.response = app.get('/healthcheck')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)


    def test_html_string_response(self):
        self.assertEqual("{ status: OK }", self.response.data.decode('utf-8'))

    # def test_content_type(self):
    #     self.assertIn('text/html', self.response.content_type)

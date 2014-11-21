from django.test import TestCase, Client
from document.models import *
from document.views import *
import string
import random

ERROR_CODES = {
        "SUCCESS": 1
        }

class DocAddTestCase(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "seth",
            "password": "tawfik",
            "confirm_password": "tawfik",
            "email": "paulina@bev.com",
        }
        client.post('/signup/', user_info)
        data = {
            "name":"test_file",
            "pdf": open('document/test.pdf')
        }
        self.response = client.post('/api/document/upload/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])


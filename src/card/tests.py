from django.test import TestCase, Client
from card.models import *
from card.views import *
import json
from django.core import serializers

ERROR_CODES = {
        "SUCCESS": 1,
        "CARD_DOESNT_EXIST": -8
        }

############
#   DECK   #
############

class DeckCreate(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userA",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)
        data = {
            "companyName": "Google",
            "companyDescription": "tech"
        }
        self.response = client.post('/api/user/create-deck/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

############
#   CARD   #
############

class AddCard(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userB",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)
        data = {
            "jobTitle": "Software Engineer",
            "status": "interested",
            "notes": "hello",
            "tags": "tech",
            "contactName": "personA",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }
        self.response = client.post('/api/card/add-card/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

# class RemoveExistingCard(TestCase):
#     def setUp(self):
#         client = Client()
#         user_info = {
#             "username": "userC",
#             "password": "password",
#             "confirm_password": "password",
#             "email": "paulina@cool.com",
#         }
#         client.post('/signup/', user_info)
#         card_data = {
#             "jobTitle": "Software Engineer",
#             "status": "interested",
#             "notes": "hello",
#             "tags": "tech",
#             "contactName": "personA",
#             "contactEmail": "poop@gmail.com",
#             "contactPhone": "123456"
#         }
#         self.response = client.post('/api/card/add-card/', card_data)
#
#         card_id_data = {
#             "card_id": "123"
#         }
#         self.response = client.post('/api/card/remove-card/', data)
#
#     def test_analyze_response(self):
#         error_code = json.loads(self.response.content)['error_message']
#         self.assertEqual(error_code, ERROR_CODES['CARD_DOESNT_EXIST'])
#
# class RemoveNonexistentCard(TestCase):
#     def setUp(self):
#         client = Client()
#         user_info = {
#             "username": "userD",
#             "password": "password",
#             "confirm_password": "password",
#             "email": "paulina@cool.com",
#         }
#         client.post('/signup/', user_info)
#         data = {
#             "card_id": "123"
#         }
#         self.response = client.post('/api/card/remove-card/', data)
#
#     def test_analyze_response(self):
#         error_code = json.loads(self.response.content)['error_message']
#         self.assertEqual(error_code, ERROR_CODES['CARD_DOESNT_EXIST'])
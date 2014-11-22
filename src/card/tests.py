from django.test import TestCase, Client
from card.models import *
from card.views import *
import json
from django.core import serializers

ERROR_CODES = {
        "SUCCESS": 1,
        "CARD_DOESNT_EXIST": -8,
        "CONTACT_DOESNT_EXIST": -14,
        "DECK_DOESNT_EXIST": -22
        }

############
#   DECK   #
############

class CreateDeck(TestCase):
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

class RemoveExistingDeck(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userAA",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)
        deck_data = {
            "companyName": "Google",
            "companyDescription": "tech"
        }
        self.create_deck_response = client.post('/api/user/create-deck/', deck_data)
        deck_id = json.loads(self.create_deck_response.content)['deck_id']

        data = {
            "deck_id": deck_id
        }

        self.response = client.post('/api/user/delete-deck/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

class RemoveNonexistentDeck(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userAAA",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        # fake data_id
        data = {
            "deck_id": "123"
        }

        self.response = client.post('/api/user/delete-deck/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['DECK_DOESNT_EXIST'])

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

        deck_data = {
            "companyName": "Google",
            "companyDescription": "tech"
        }
        self.create_deck_response = client.post('/api/user/create-deck/', deck_data)
        deck_id = json.loads(self.create_deck_response.content)['deck_id']

        data = {
            "deck_id": deck_id,
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
#
#         deck_data = {
#             "companyName": "Google",
#             "companyDescription": "tech"
#         }
#         self.create_deck_response = client.post('/api/user/create-deck/', deck_data)
#         deck_id = json.loads(self.create_deck_response.content)['deck_id']
#
#         card_data = {
#             "deck_id": deck_id,
#             "jobTitle": "Software Engineer",
#             "status": "interested",
#             "notes": "hello",
#             "tags": "tech",
#             "contactName": "personA",
#             "contactEmail": "poop@gmail.com",
#             "contactPhone": "123456"
#         }
#
#
#         self.add_card_response = client.post('/api/card/add-card/', card_data)
#         card_id = json.loads(self.add_card_response.content)['card_id']
#         data = {
#             "card_id": card_id
#         }
#
#         self.response = client.post('/api/user/remove-card/', data)
#
#
#     def test_analyze_response(self):
#         error_code = json.loads(self.response.content)['error_message']
#         self.assertEqual(error_code, ERROR_CODES['SUCCESS'])
#
# class RemoveNonexistentCard(TestCase):
#     def setUp(self):
#         client = Client()
#         user_info = {
#             "username": "userBBB",
#             "password": "password",
#             "confirm_password": "password",
#             "email": "paulina@cool.com",
#         }
#         client.post('/signup/', user_info)
#
#         # fake card_id
#         data = {
#             "card_id": "123"
#         }
#
#         self.response = client.post('/api/user/remove-card/', data)
#
#
#     def test_analyze_response(self):
#         error_code = json.loads(self.response.content)['error_message']
#         self.assertEqual(error_code, ERROR_CODES['CARD_DOESNT_EXIST'])

################
#   CONTACTS   #
################

class AddContact(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userC",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        deck_data = {
            "companyName": "Google",
            "companyDescription": "tech"
        }
        self.create_deck_response = client.post('/api/user/create-deck/', deck_data)
        deck_id = json.loads(self.create_deck_response.content)['deck_id']

        card_data = {
            "deck_id": deck_id,
            "jobTitle": "Software Engineer",
            "status": "interested",
            "notes": "hello",
            "tags": "tech",
            "contactName": "personA",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }

        self.add_card_response = client.post('/api/card/add-card/', card_data)
        card_id = json.loads(self.add_card_response.content)['card_id']

        data = {
            "card_id": card_id,
            "add_name": "Alex",
            "add_email": "alex@wang.com",
            "add_phone": "1234567890"
        }

        self.response = client.post('/api/card/add-contact/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

class RemoveNonexistentContact(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userCC",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        deck_data = {
            "companyName": "Google",
            "companyDescription": "tech"
        }
        self.create_deck_response = client.post('/api/user/create-deck/', deck_data)
        deck_id = json.loads(self.create_deck_response.content)['deck_id']

        card_data = {
            "deck_id": deck_id,
            "jobTitle": "Software Engineer",
            "status": "interested",
            "notes": "hello",
            "tags": "tech",
            "contactName": "personA",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }

        self.add_card_response = client.post('/api/card/add-card/', card_data)
        card_id = json.loads(self.add_card_response.content)['card_id']

        data = {
            "card_id": card_id,
            "contactName": "Nonexistent Person"
        }

        self.response = client.post('/api/card/remove-contact/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['CONTACT_DOESNT_EXIST'])

################
#   TAGS   #
################

class AddTag(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userD",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        deck_data = {
            "companyName": "Google",
            "companyDescription": "tech"
        }
        self.create_deck_response = client.post('/api/user/create-deck/', deck_data)
        deck_id = json.loads(self.create_deck_response.content)['deck_id']

        card_data = {
            "deck_id": deck_id,
            "jobTitle": "Software Engineer",
            "status": "interested",
            "notes": "hello",
            "tags": "tech",
            "contactName": "personA",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }

        self.add_card_response = client.post('/api/card/add-card/', card_data)
        card_id = json.loads(self.add_card_response.content)['card_id']

        data = {
            "card_id": card_id,
            "tags": "tech,food,fun"
        }

        self.response = client.post('/api/card/add-tag/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

class RemoveTag(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userDD",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        deck_data = {
            "companyName": "Google",
            "companyDescription": "tech"
        }
        self.create_deck_response = client.post('/api/user/create-deck/', deck_data)
        deck_id = json.loads(self.create_deck_response.content)['deck_id']

        card_data = {
            "deck_id": deck_id,
            "jobTitle": "Software Engineer",
            "status": "interested",
            "notes": "hello",
            "tags": "tech",
            "contactName": "personA",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }

        self.add_card_response = client.post('/api/card/add-card/', card_data)
        card_id = json.loads(self.add_card_response.content)['card_id']

        tag_data = {
            "card_id": card_id,
            "tags": "tech,food,fun"
        }

        client.post('/api/card/add-tag/', tag_data)

        data = {
            "card_id": card_id,
            "target_tag": "food"
        }

        self.response = client.post('/api/card/remove-tag/', data)

        self.test = client.get('/api/card/get-tags/', {"card_id": card_id})

        if "food" in self.test:
            print "tag deletion did not work"

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])


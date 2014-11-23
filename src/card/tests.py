<<<<<<< HEAD
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

class RemoveExistingCard(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userBB",
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
            "card_id": card_id
        }

        self.response = client.post('/api/user/remove-card/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

class RemoveNonexistentCard(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userBBB",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        # fake card_id
        data = {
            "card_id": "123"
        }

        self.response = client.post('/api/user/remove-card/', data)


    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['CARD_DOESNT_EXIST'])

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

class RemoveExistingContact(TestCase):
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
            "contactName": "personA"
        }

        self.response = client.post('/api/card/remove-contact/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

class RemoveNonexistentContact(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userCCC",
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

class EditContact(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userCCCC",
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
            "contactName": "Bob",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }

        self.add_card_response = client.post('/api/card/add-card/', card_data)
        card_id = json.loads(self.add_card_response.content)['card_id']

        data = {
            "card_id": card_id,
            "current_name": "Bob",
            "new_name": "Alice",
            "new_email": "alice@gmail.com",
            "new_phone": "111111"
        }

        self.response = client.post('/api/card/edit-contact/', data)

        self.contacts = client.get('/api/card/get-contacts/', {"card_id": card_id})
        if "Alice" not in self.contacts.content:
            print "edit_contact was unsuccessful"

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

class GetContacts(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userCCCCC",
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
            "contactName": "Bob",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }

        self.add_card_response = client.post('/api/card/add-card/', card_data)
        card_id = json.loads(self.add_card_response.content)['card_id']

        self.contacts = client.get('/api/card/get-contacts/', {"card_id": card_id})

    def test_analyze_response(self):
        self.assertTrue("Bob" in self.contacts.content)

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

class GetTags(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userDDD",
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
            "tags": "tech,food,fun",
            "contactName": "personA",
            "contactEmail": "poop@gmail.com",
            "contactPhone": "123456"
        }

        self.add_card_response = client.post('/api/card/add-card/', card_data)
        card_id = json.loads(self.add_card_response.content)['card_id']

        self.tags = client.get('/api/card/get-tags/', {"card_id": card_id})

    def test_analyze_response(self):
        self.assertTrue("fun" in self.tags.content)

class EditTag(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userDDDD",
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
            "tags": "food,fun"
        }

        client.post('/api/card/add-tag/', tag_data)

        data = {
            "card_id": card_id,
            "tag_to_replace": "food",
            "new_tag": "drinks"
        }

        self.response = client.post('/api/card/edit-tag/', data)

        self.test = client.get('/api/card/get-tags/', {"card_id": card_id})

        if "food" in self.test:
            print "edit tag did not work"

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

##############
#   STATUS   #
##############

class ModifyStatus(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userE",
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
            "new_status": "complete"
        }

        self.response = client.post('/api/card/modify-card-status/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])


class ModifyStatusCardNonexistent(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userEE",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        data = {
            "card_id": "123",
            "new_status": "rejected"
        }

        self.response = client.post('/api/card/modify-card-status/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['CARD_DOESNT_EXIST'])

#############
#   NOTES   #
#############

class EditNotes(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userF",
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
            "new_notes": "goodbye"
        }

        self.response = client.post('/api/card/edit-notes/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

class EditNotesCardNonexistent(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userFF",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        data = {
            "card_id": "123",
            "new_notes": "goodbye"
        }

        self.response = client.post('/api/card/edit-notes/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['CARD_DOESNT_EXIST'])

#############
#   TASKS   #
#############

class EditNotes(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userG",
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
            "new_task": "follow up with recruiter"
        }

        self.response = client.post('/api/card/add-task/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])
=======
"""
Unit tests UserApp, CardApp, and DocumentApp.
"""


from django.test import TestCase, Client
from card.models import *
from card.views import *
import string
import random

class GoodAddTestCase(TestCase):
    def setUp(self):
        client = Client()
        self.response = client.get('/api/card/all-cards/', {})

    def test_analyze_response(self):
        print(self.response.content)
        #error_code = simplejson.loads(self.response.content)['errCode']
        #self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

#class TestCard(unittest.TestCase):
#    """
#    Unit tests for the Card class (part of CardApp)
#    """
#    cards = views.Card()
#
#    ###################
#    ##               ##
#    ##  CREATE CARD  ##
#    ##               ##
#    ###################
#
#    def testCreateCard(self):
#        """
#        Tests that a card can be created.
#        """
#        print dir(self.cards)
#        self.assertEqual(1, self.cards.create_card("Amazon", "Software Engineer", "in-progress"))
#
#    def testCreateCardLongCompanyName(self):
#        """
#        Tests that creating a card with a company name that exceeds 128 characters fails.
#        """
#        long_name = "LongCompanyName"*10
#        self.assertEqual(0, self.cards.create_card(long_name, "Software Engineer", "in-progress"))
#
#    def testCreateCardEmptyCompanyName(self):
#        """
#        Tests that creating a card with an empty company name fails.
#        """
#        self.assertEqual(0, self.cards.create_card("", "Software Engineer", "in-progress"))
#
#    def testCreateCardNoneCompanyName(self):
#        """
#        Tests that creating a card with a None company name fails.
#        """
#        self.assertEqual(0, self.cards.create_card(None, "Software Engineer", "in-progress"))
#
#    def testCreateCardLongJobTitle(self):
#        """
#        Tests that creating a card with a job title that exceeds 128 characters fails.
#        """
#        long_title = "LongJobTitle"*10
#        self.assertEqual(0, self.cards.create_card("Accenture", long_title, "in-progress"))
#
#    def testCreateCardEmptyJobTitle(self):
#        """
#        Tests that creating a card with an empty job title fails.
#        """
#        self.assertEqual(0, self.cards.create_card("AirPR", "", "in-progress"))
#
#    def testCreateCardNoneJobTitle(self):
#        """
#        Tests that creating a card with a None job title fails.
#        """
#        self.assertEqual(0, self.cards.create_card("Affirm", None, "in-progress"))
#
#    # def testCreateCardInvalidStatus(self):
#    #     """
#    #     Tests that creating a card with a status that is not 0, 1, or 2 fails.
#    #     """
#    #     self.assertEqual(0, self.cards.create_card("BrightRoll", "Software Engineer", 3))
#
#    def testCreateCardsConsecutively(self):
#        """
#        Tests that consecutive cards of different statuses can be created.
#        """
#        self.assertEqual(1, self.cards.create_card("Apple", "Software Engineer", "in-progress"))
#        self.assertEqual(1, self.cards.create_card("Airbnb", "Software Engineer", "offered"))
#        self.assertEqual(1, self.cards.create_card("Akamai", "Software Engineer", "rejected"))
#
#    ###################
#    ##               ##
#    ##  MODIFY CARD  ##
#    ##               ##
#    ###################
#
#    def testModifyCard(self):
#        """
#        Tests that a card's status can be modified.
#        """
#        self.assertEqual(1, self.cards.create_card("Boeing", "Mechanical Engineer", "in-progress"))
#        card_id = models.Card.objects.get(name='Boeing').id
#        self.assertEqual(1, self.cards.change_status(card_id, "rejected"))
#
#    # def testModifyCardInvalidStatus(self):
#    #     """
#    #     Tests that a card's status can't be modified to an invalid status number.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("Behance", "Web Developer", 1))
#    #     card_id = models.Card.objects.get(name='Behance').id
#    #     self.assertEqual(0, self.cards.change_status(card_id, 3))
#
################################################################################################################
#
#class TestTag(unittest.TestCase):
#    """
#    Unit tests for the Tag class (part of CardApp)
#    """
#    tags = models.Tag()
#    cards = models.Card()
#
#    ###############
#    ##           ##
#    ##  ADD TAG  ##
#    ##           ##
#    ###############
#
#    def testAddTag(self):
#        """
#        Tests that a tag between 1-128 characters can be added to an existing card.
#        """
#        self.assertEqual(1, self.cards.create_card("Capricity", "Software Engineer", "in-progress"))
#        card_id = models.Card.objects.get(name='Capricity').id
#        self.assertEqual(1, self.tags.add_tag(card_id, "tech"))
#
#    def testAddTagLong(self):
#        """
#        Tests that adding a tag that exceeds 128 characters fails.
#        """
#        self.assertEqual(1, self.cards.create_card("CompanyA", "Software Engineer", "in-progress"))
#        card_id = models.Card.objects.get(name='CompanyA').id
#        long_tag = "technologyrocksssss"*10
#        self.assertEqual(0, self.tags.add_tag(card_id, long_tag))
#
#    def testAddTagEmpty(self):
#        """
#        Tests that adding an empty tag fails.
#        """
#        self.assertEqual(1, self.cards.create_card("CompanyB", "Software Engineer", "in-progress"))
#        card_id = models.Card.objects.get(name='CompanyB').id
#        self.assertEqual(0, self.tags.add_tag(card_id, ""))
#
#    def testAddTagNone(self):
#        """
#        Tests that adding a None tag fails.
#        """
#        self.assertEqual(1, self.cards.create_card("CompanyC", "Software Engineer", "in-progress"))
#        card_id = models.Card.objects.get(name='CompanyC').id
#        self.assertEqual(0, self.tags.add_tag(card_id, None))
#
#    def testAddCardIDEmpty(self):
#        """
#        Tests that adding a tag to an empty card ID fails.
#        """
#        self.assertEqual(0, self.tags.add_tag("", "tech"))
#
#    def testAddCardIDNone(self):
#        """
#        Tests that adding a tag to a None card ID fails.
#        """
#        self.assertEqual(0, self.tags.add_tag(None, "tech"))
#
#    def testAddCardIDNonexistent(self):
#        """
#        Tests that adding a tag to a card that doesn't exist fails.
#        """
#        self.assertEqual(0, self.tags.add_tag(models.Card.objects.get(name='THIS_CARD_DOESNT_EXIST').id,
#                                                           "tech"))
#
#    ##################
#    ##              ##
#    ##  MODIFY TAG  ##
#    ##              ##
#    ##################
#
#    # def testModifyTag(self):
#    #     """
#    #     Tests that modifying a card's tag with a new tag between 1-128 characters succeeds.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyD", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyD').id
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "tech"))
#    #     self.assertEqual(1, self.tags.modify_tag(card_id, "tech", "engineer"))
#    #
#    # def testModifyTagLong1(self):
#    #     """
#    #     Tests that modifying a card's tag with a new tag that exceeds 128 characters fails.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyE", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyE').id
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "tech"))
#    #     new_long_tag = "superlongtagahhhhhh"*10
#    #     self.assertEqual(0, self.tags.modify_tag(card_id, "tech", new_long_tag))
#    #
#    # def testModifyTagLong2(self):
#    #     """
#    #     Tests that passing in a current_tag_name that is over 128 characters fails.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyF", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyF').id
#    #     long_current_tag = "superlongtagahhhhhh"*10
#    #     self.assertEqual(0, self.tags.modify_tag(card_id, long_current_tag, "shorter_tag"))
#    #
#    # def testModifyTagNonexistentCard(self):
#    #     """
#    #     Tests that modifying a tag on a card that doesn't exist fails.
#    #     """
#    #     self.assertEqual(0, self.tags.modify_tag(models.Card.objects.get(name='NONEXISTENT_COMPANY').id,
#    #                                                           "hardware", "software"))
#    #
#    # def testModifyTagNonexistent(self):
#    #     """
#    #     Tests that passing in a current_tag_name that doesn't exist fails.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyG", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyG').id
#    #     self.assertEqual(0, self.tags.modify_tag(card_id, "this_tag_doesnt_exist", "new_tag"))
#    #
#    # def testModifyTagDuplicate(self):
#    #     """
#    #     Tests that modifying a tag to one that already exists will fail.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyH", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyH').id
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "tech"))
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "engineer"))
#    #     self.assertEqual(0, self.tags.modify_tag(card_id, "tech", "engineer"))
#
#    ################
#    ##            ##
#    ##  GET TAGS  ##
#    ##            ##
#    ################
#
#    # def testGetTags(self):
#    #     """
#    #     Tests that it returns a list of tags associated with an existing card_id.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyI", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyI').id
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "tech"))
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "software"))
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "engineer"))
#    #     tags_list = ["tech", "software", "engineer"]
#    #     self.assertEqual(tags_list, self.tags.get_tags(card_id))
#    #
#    # def testGetTagsInvalidCard(self):
#    #     """
#    #     Tests that it doesn't return a list of tags for a non-existent card id.
#    #     """
#    #     self.assertEqual(0, self.tags.get_tags("THIS_CARD_ID_DOESNT_EXIST"))
#
#    ###################
#    ##               ##
#    ##  REMOVE TAGS  ##
#    ##               ##
#    ###################
#
#    # def testRemoveTagInvalidCard(self):
#    #     """
#    #     Tests that it fails to removes an existing tag from a non-existent card.
#    #     """
#    #     self.assertEqual(0, self.tags.remove_tag("THIS_CARD_ID_DOESNT_EXIST", "tech"))
#    #
#    # def testRemoveTagNonexistentTag(self):
#    #     """
#    #     Tests that it fails to removes a non-existent tag from an existing card.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyJ", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyJ').id
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "software"))
#    #     self.assertEqual(0, self.tags.remove_tag(card_id, "hardware"))
#    #
#    # def testRemoveTag(self):
#    #     """
#    #     Tests that it successfully removes an existing tag from an existing card.
#    #     """
#    #     self.assertEqual(1, self.cards.create_card("CompanyK", "Software Engineer", "in-progress"))
#    #     card_id = models.Card.objects.get(name='CompanyK').id
#    #     self.assertEqual(1, self.tags.add_tag(card_id, "tech"))
#    #     self.assertEqual(1, self.tags.remove_tag(card_id, "tech"))
#
## If this file is invoked as a Python script, run the tests in this module
#if __name__ == "__main__":
#    # Add a verbose argument
#    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
#    unittest.main()
>>>>>>> 2af7208e384aaf04ca959db7c1e0ae0d37a15dde

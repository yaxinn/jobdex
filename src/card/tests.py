from django.test import TestCase, Client
from card.models import *
from card.views import *
from document.models import *
from document.views import *
import json
from django.core import serializers

ERROR_CODES = {
        "SUCCESS": 1,
        "CARD_DOESNT_EXIST": -8,
        "DOCUMENT_DOESNT_EXIST": -11,
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

class GetDeck(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "user36435645",
            "password": "password",
            "confirm_password": "password",
            "email": "paul@cool.com",
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
        # self.response2 = client.post('/api/card/all-cards/')

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])

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
#   NOTES   #
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

##########################
#   DOCUMENTS PER CARD   #
##########################

class AddNonexistentDocument(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userH",
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
            "document": "my resume doesn't exist"
        }

        self.response = client.post('/api/card/add-document/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['DOCUMENT_DOESNT_EXIST'])

class AddDocumentNonexistentCard(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userHH",
            "password": "password",
            "confirm_password": "password",
            "email": "paulina@cool.com",
        }
        client.post('/signup/', user_info)

        data = {
            "card_id": "123",
            "document": "my resume doesn't exist"
        }

        self.response = client.post('/api/card/add-document/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['CARD_DOESNT_EXIST'])

class AddExistingDocument(TestCase):
    def setUp(self):
        client = Client()
        user_info = {
            "username": "userHHH",
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

        document_data = {
            "name": "test_file",
            "pdf": open('document/test.pdf')
        }

        client.post('/api/document/upload/', document_data)

        data = {
            "card_id": card_id,
            "document": "test_file"
        }

        self.response = client.post('/api/card/add-document/', data)

    def test_analyze_response(self):
        error_code = json.loads(self.response.content)['error_message']
        self.assertEqual(error_code, ERROR_CODES['SUCCESS'])
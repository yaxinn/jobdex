"""
Run with "python -m unittest discover -v" in /src/.
"""

import unittest
import os
from django.test import Client
import django
import traceback
import httplib
import sys
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobdex.settings")
django.setup()

##################
### HTML TESTS ###
##################

class TestAbout(testLib.RestTestCase):
	def test_about(self):
		self.client = Client()
		response = self.client.get("/about/")
		self.assertEqual(response.status_code, 200)

class TestReport(testLib.RestTestCase):
	def test_report(self):
		self.client = Client()
		response = self.client.get("/report/")
		self.assertEqual(response.status_code, 200)

class TestReport(testLib.RestTestCase):
	def test_report(self):
		self.client = Client()
		response = self.client.get("/report/")
		self.assertEqual(response.status_code, 200)


###################
### LOGIN TESTS ###
###################

class TestAddUser(testLib.RestTestCase):
	def test_signup(self):
		self.client = Client(enforce_csrf_checks=True)
		self.client.get("/")
		csrf = self.client.cookies['csrftoken'].value
		response = self.client.post('/signup/', 
			{ 'csrfmiddlewaretoken' : csrf, 
			'username' : 'usernumber1',
			'password' : 'password', 
			'confirm_password' : 'password',
			'email' : 'usernumber1@gmail.com' })
		self.assertEqual(response.status_code, 200)

class TestLogout(testLib.RestTestCase):
	def test_signup(self):
		self.client = Client()
		response = self.client.get("/logout/")
		self.assertEqual(response.status_code, 302)

class TestLogin(testLib.RestTestCase):
	def test_login(self):
		self.client = Client(enforce_csrf_checks=True)
		self.client.get("/")
		csrf = self.client.cookies['csrftoken'].value
		response = self.client.post('/login/', 
			{ 'csrfmiddlewaretoken' : csrf, 
			'username' : 'usernumber1',
			'password' : 'password' })
		self.assertIsNot(response.status_code, 500)


##################
### CARD TESTS ###
##################

class TestAddCard(testLib.RestTestCase):
	def test_add_card(self):
		response = Client().post('api/user/create-card',
			{ "company-name" : "Jobdex",
			"status" : "Complete",
			"tags" : "fun, exciting",
			"notes" : "cool job!",
			"position" : "Water Boy",
			"contact-name" : "Paul Tawfik",
			"contact-email" : "paul@gmail.com",
			"contact-phone" : "1234567890" })
		self.assertIsNot(response.status_code, 500)

class TestAddMultipleCards(testLib.RestTestCase):
	def test_add_multiple_cards(self):
		response = Client().post('api/user/create-card',
			{ "company-name" : "Jobdex",
			"status" : "Complete",
			"tags" : "fun, exciting",
			"notes" : "cool job!",
			"position" : "Water Boy",
			"contact-name" : "Paul Tawfik",
			"contact-email" : "paul@gmail.com",
			"contact-phone" : "1234567890" })
		self.assertIsNot(response.status_code, 500)
		response = Client().post('api/user/create-card',
			{ "company-name" : "Jobdex",
			"status" : "Complete",
			"tags" : "fun, exciting",
			"notes" : "cool job!",
			"position" : "Water Boy",
			"contact-name" : "Paul Tawfik",
			"contact-email" : "paul@gmail.com",
			"contact-phone" : "1234567890" })
		self.assertIsNot(response.status_code, 500)

class TestEmptyCard(testLib.RestTestCase):
	def test_add_empty_card(self):
		response = Client().post('api/user/create-card',
			{ "company-name" : "",
			"status" : "",
			"tags" : "",
			"notes" : "",
			"position" : "",
			"contact-name" : "",
			"contact-email" : "",
			"contact-phone" : "" })
		self.assertIsNot(response.status_code, 500)

class TestLongTitle(testLib.RestTestCase):
	def test_add_card(self):
		title = "LongJobTitle"*10
		response = Client().post('api/user/create-card',
			{ "company-name" : title,
			"status" : "Complete",
			"tags" : "fun, exciting",
			"notes" : "cool job!",
			"position" : "Water Boy",
			"contact-name" : "Paul Tawfik",
			"contact-email" : "paul@gmail.com",
			"contact-phone" : "1234567890" })
		self.assertIsNot(response.status_code, 500)

"""
Run with "python -m unittest discover -v" in /src/.
"""

import unittest
import os
import testLib
from django.test import Client
import django
import traceback
import httplib
import sys
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobdex.settings")
django.setup()

class TestSignup(testLib.RestTestCase):
	def test_signup(self):
		client = Client(enforce_csrf_checks=True)
		client.get("/")
		csrf = client.cookies['csrftoken'].value
		response = client.post("/signup/", {
			'csrfmiddlewaretoken': csrf,
			'username': 'Barack', 
			'password': 'Obama', 
			'confirm_password': 'Obama', 
			'email': 'romneysucks@gmail.com'
		})

class TestAddCard(testLib.RestTestCase):
	def test_add_card(self):
		client = Client()
		response = client.post('/api/user/create-deck/', {
			'companyName': 'Apple',
			'companyDescription': 'Overpriced and crappy.'
			})
		deckID = json.loads(response.content)['deck_id']
		print(deckID)

"""
class TestLoginBeforeAdd(testLib.RestTestCase):
	def testLoginBeforeAdd(self):
		self.user = "bobthebuilder"
		self.password = "jobtheweilder"
		respData = self.makeRequest("/users/login", method="POST", data={'user':self.user, 'password':self.password})
		self.assertEquals(self.ERR_BAD_CREDENTIALS, respData['errCode'])

class TestAddMany(testLib.RestTestCase):
	def testAddMany(self):
		self.num_add = 100
		for i in xrange(self.num_add):
			respData = self.makeRequest("/users/add", method="POST", data={'user':str(i), 'password':"pass"})
			self.assertEquals(self.SUCCESS, respData['errCode'])

class TestBadPassword(testLib.RestTestCase):
	def testBadPassword(self):
		self.user = "asdf"
		self.password = ""
		for _ in xrange(129):
			self.password += "a"
		respData = self.makeRequest("/users/add", method="POST", data={'user':self.user, 'password':self.password})
		self.assertEquals(self.ERR_BAD_PASSWORD, respData['errCode'])

class TestAddSame(testLib.RestTestCase):
	def testAddSame(self):
		self.user = "asdf"
		self.password = "fdsa"
		respData = self.makeRequest("/users/add", method="POST", data={'user':self.user, 'password':self.password})
		self.assertEquals(self.SUCCESS, respData['errCode'])
		respData = self.makeRequest("/users/add", method="POST", data={'user':self.user, 'password':self.password})
		self.assertEquals(self.ERR_USER_EXISTS, respData['errCode'])

class TestMultipleCounts(testLib.RestTestCase):
	def testMultipleCounts(self):
		self.firstUser = "User numba 1"
		self.secondUser = "User numba 2"
		self.password = "sharedPass"
		self.firstCount = random.randint(1, 20)
		self.secondCount = random.randint(1, 20)
		respData = self.makeRequest("/users/add", method="POST", data={'user':self.firstUser, 'password':self.password})
		self.assertEquals(1, respData['count'])
		respData = self.makeRequest("/users/add", method="POST", data={'user':self.secondUser, 'password':self.password})
		self.assertEquals(1, respData['count'])
		for _ in xrange(self.firstCount):
			respData = self.makeRequest("/users/login", method="POST", data={'user':self.firstUser, 'password':self.password})
			self.assertEquals(self.SUCCESS, respData['errCode'])
		self.assertEquals(self.firstCount, respData['count'])
		for _ in xrange(self.secondCount):
			respData = self.makeRequest("/users/login", method="POST", data={'user':self.secondUser, 'password':self.password})
			self.assertEquals(self.SUCCESS, respData['errCode'])
		self.assertEquals(self.secondCount, respData['count'])
"""
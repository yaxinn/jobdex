from django.test import TestCase, Client
from document.models import *
from document.views import *
import string
import random

ERROR_CODES = {
        "SUCCESS": 1,
        "DOCEXIST": -9,
        "DOCINVALID": -10,
        "DOCDNEXIST": -11,
        "REDIRECT": 302
        }

# add document test
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
            "name": "test_file",
            "pdf": open('document/test.pdf')
        }
        self.response = client.post('/api/document/upload/', data)

    def test_analyze_response(self):
        self.assertEqual(self.response.status_code, ERROR_CODES['REDIRECT'])

# add existing document test
# class DocAddExistTestCase(TestCase):
# 	def setUp(self):
# 		client = Client()
# 		user_info = {
# 			"username": "seth",
# 			"password": "tawfik",
# 			"confirm_password": "tawfik",
# 			"email": "paulina@bev.com",
# 		}
# 		client.post('/signup/', user_info)
# 		data = {
# 			"name": "test_file",
# 			"pdf": open('document/test.pdf')
# 		}
# 		client.post('/api/document/upload/', data)
# 		self.response = client.post('/api/document/upload/', data)
#
# 	def test_analyze_response(self):
# 		error_code = json.loads(self.response.content)['error_message']
# 		self.assertEqual(error_code, ERROR_CODES['DOCEXIST'])

# get document test
class DocGetTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		user_info = {
			"username": "seth",
			"password": "tawfik",
			"confirm_password": "tawfik",
			"email": "paulina@bev.com", 
		}
		self.client.post('/signup/', user_info)

	def test_analyze_response(self):
		data = {"name": "test_file",
					   "pdf": open('document/test.pdf')}
		self.client.post('/api/document/upload/', data)
		self.response = self.client.get('/api/document/get/', {})
		content = json.loads(self.response.content)
		l = len(content)
		self.assertEqual(1, l)
		self.assertEqual(True, "test_file" in content)


# delete existing document test
class DocDelTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		user_info = {
			"username": "seth",
			"password": "tawfik",
			"confirm_password": "tawfik",
			"email": "paulina@bev.com", 
		}
		self.client.post('/signup/', user_info)

	def test_analyze_response(self):
		upload_data = {"name": "test_file",
					   "pdf": open('document/test.pdf')}

		# send a request to upload doc and a request to get doc list
		self.client.post('/api/document/upload/', upload_data)
		self.get_response = self.client.get('/api/document/get/', {})
		content = json.loads(self.get_response.content)
 		l1 = len(content)

  	    # send a request to delete doc and a request to get doc list
		delete_data = {"doc_id": content["test_file"]["unique_id"]}

		self.response = self.client.post('/api/document/delete/', delete_data)
		self.get_response = self.client.get('/api/document/get/', {})
		content = json.loads(self.get_response.content)
		l2 = len(content)

		error_code = json.loads(self.response.content)['error_message']
		self.assertEqual(error_code, ERROR_CODES['SUCCESS'])
		self.assertEqual(1, l1-l2)

# delete document that doens't exist
class DocDelDNETestCase(TestCase):
	def setUp(self):
		self.client = Client()
		user_info = {
			"username": "seth",
			"password": "tawfik",
			"confirm_password": "tawfik",
			"email": "paulina@bev.com", 
		}
		self.client.post('/signup/', user_info)

	def test_analyze_response(self):
		test_id = "ab337910-abe6-4848-ac51-f262df2d8a79"
		data = {"doc_id": test_id}
		self.response = self.client.post('/api/document/delete/', data)
		error_code = json.loads(self.response.content)['error_message']
		self.assertEqual(error_code, ERROR_CODES['DOCDNEXIST'])

# add .doc format document test
class DocTypeTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		user_info = {
			"username": "seth",
			"password": "tawfik",
			"confirm_password": "tawfik",
			"email": "paulina@bev.com", 
		}
		self.client.post('/signup/', user_info)

	def test_analyze_response(self):
		data = {"name": "test_doc", 
				"pdf": open('document/test.doc')}
		self.response = self.client.post('/api/document/upload/', data)
		error_code = json.loads(self.response.content)['error_message']
		self.assertEqual(error_code, ERROR_CODES['DOCINVALID'])
"""Functional tests."""

import unittest
import os
import testLib

import unittest
import sys
import models

class TestCard(testLib.RestTestCase):
    """Tests Card controllers"""

    cards = models.Card()

    # def testCardCreate(self):
    #     jsonObj = {
    #                 'companyName' : 'Amazon',
    #                 'status' : 'in-progress',
    #                 'jobTitle' : 'Software Engineer',
    #                 'tags' : 'tech',
    #                 'contactName' : 'Bob',
    #                 'contactEmail' : 'bobsmith@gmail.com',
    #                 'contactPhone' : '5101234567'
    #               }
    #     respData = self.makeRequest("/user/create-card",
    #                                 method = "POST",
    #                                 data = jsonObj)
    #     expectedResponse = {'card_id': card_id, 'error_code': 1}
    #     self.assertDictEqual(respData, expectedResponse)


    def testModifyCardStatus(self):
        self.tags.create_card("CompanyJ", "Software Engineer", "accepted")
        card_id = str(models.Card.objects.get(name='CompanyJ').id)
        new_status = "rejected"
        jsonObj = {
                    'card_id' : card_id,
                    'status' : new_status
                  }
        respData = self.makeRequest("/card/" + card_id + "/change-status",
                                    method = "POST",
                                    data = jsonObj)
        expectedResponse = {'error_message': 1}
        self.assertDictEqual(respData, expectedResponse)

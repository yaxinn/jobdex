"""
Unit tests UserApp, CardApp, and DocumentApp.
"""

import unittest
import sys
import models

class TestDocument(unittest.TestCase):
    """
    Unit tests for the Document class (part of DocumentApp)
    """
    documents = models.Documents()

    ######################
    ##                  ##
    ##  REMOVE DOCUMENT ##
    ##                  ##
    ######################

    def testRemoveDocumentNonexistentID(self):
        """
        Tests that removing a document that doesn't exist will fail.
        """
        self.assertEqual(models.FAILURE, self.documents.remove_document("NONEXISTENT_DOCUMENT_ID"))

    def testRemoveDocumentNonexistentID(self):
        """
        Tests that removing a document id that
        """
        self.assertEqual(models.FAILURE, self.documents.remove_document("NONEXISTENT_DOCUMENT_ID"))

    ####################
    ##                ##
    ##  GET DOCUMENTS ##
    ##                ##
    ####################

    def testGetDocumentsNonexistentUser(self):
        """
        Tests that getting documents belonging to a non-existent user will fail.
        """
        self.assertEqual(models.FAILURE, self.documents.get_documents("NONEXISTENT_USER_ID"))

    def testGetDocumentsLongUsername(self):
        """
        Tests that passing in a user_id that exceeds 128 characters will fail.
        """
        long_user_id = "thisisasuperlonguserid"*10
        self.assertEqual(models.FAILURE, self.documents.get_documents(long_user_id))

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
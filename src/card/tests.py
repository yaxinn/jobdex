"""
Unit tests UserApp, CardApp, and DocumentApp.
"""

import unittest
import sys
import models

class TestCard(unittest.TestCase):
    """
    Unit tests for the Card class (part of CardApp)
    """
    cards = models.Card()

    ###################
    ##               ##
    ##  CREATE CARD  ##
    ##               ##
    ###################

    def testCreateCard(self):
        """
        Tests that a card can be created.
        """
        self.assertEqual(models.SUCCESS, self.cards.create_card("Amazon", "Software Engineer", 2))

    def testCreateCardLongCompanyName(self):
        """
        Tests that creating a card with a company name that exceeds 128 characters fails.
        """
        long_name = "LongCompanyName"*10
        self.assertEqual(models.FAILURE, self.cards.create_card(long_name, "Software Engineer", 2))

    def testCreateCardEmptyCompanyName(self):
        """
        Tests that creating a card with an empty company name fails.
        """
        self.assertEqual(models.FAILURE, self.cards.create_card("", "Software Engineer", 2))

    def testCreateCardNoneCompanyName(self):
        """
        Tests that creating a card with a None company name fails.
        """
        self.assertEqual(models.FAILURE, self.cards.create_card(None, "Software Engineer", 2))

    def testCreateCardLongJobTitle(self):
        """
        Tests that creating a card with a job title that exceeds 128 characters fails.
        """
        long_title = "LongJobTitle"*10
        self.assertEqual(models.FAILURE, self.cards.create_card("Accenture", long_title, 2))

    def testCreateCardEmptyJobTitle(self):
        """
        Tests that creating a card with an empty job title fails.
        """
        self.assertEqual(models.FAILURE, self.cards.create_card("AirPR", "", 2))

    def testCreateCardNoneJobTitle(self):
        """
        Tests that creating a card with a None job title fails.
        """
        self.assertEqual(models.FAILURE, self.cards.create_card("Affirm", None, 2))

    def testCreateCardInvalidStatus(self):
        """
        Tests that creating a card with a status that is not 0, 1, or 2 fails.
        """
        self.assertEqual(models.FAILURE, self.cards.create_card("BrightRoll", "Software Engineer", 3))

    def testCreateCardsConsecutively(self):
        """
        Tests that consecutive cards of different statuses can be created.
        """
        self.assertEqual(models.SUCCESS, self.cards.create_card("Apple", "Software Engineer", 0))
        self.assertEqual(models.SUCCESS, self.cards.create_card("Airbnb", "Software Engineer", 1))
        self.assertEqual(models.SUCCESS, self.cards.create_card("Akamai", "Software Engineer", 2))

    ###################
    ##               ##
    ##  MODIFY CARD  ##
    ##               ##
    ###################

    def testModifyCard(self):
        """
        Tests that a card's status can be modified.
        """
        self.assertEqual(models.SUCCESS, self.cards.create_card("Boeing", "Mechanical Engineer", 1))
        card_id = models.Card.objects.get(name='Boeing').id
        self.assertEqual(models.SUCCESS, self.cards.change_status(card_id, 0))

    def testModifyCardInvalidStatus(self):
        """
        Tests that a card's status can't be modified to an invalid status number.
        """
        self.assertEqual(models.SUCCESS, self.cards.create_card("Behance", "Web Developer", 1))
        card_id = models.Card.objects.get(name='Behance').id
        self.assertEqual(models.FAILURE, self.cards.change_status(card_id, 3))

###############################################################################################################

class TestTag(unittest.TestCase):
    """
    Unit tests for the Tag class (part of CardApp)
    """
    tags = models.Tag()

    ###############
    ##           ##
    ##  ADD TAG  ##
    ##           ##
    ###############

    def testAddTag(self):
        """
        Tests that a tag between 1-128 characters can be added to an existing card.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("Capricity", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='Capricity').id
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "tech"))

    def testAddTagLong(self):
        """
        Tests that adding a tag that exceeds 128 characters fails.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyA", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyA').id
        long_tag = "technologyrocksssss"*10
        self.assertEqual(models.FAILURE, self.tags.add_tag(card_id, long_tag))

    def testAddTagEmpty(self):
        """
        Tests that adding an empty tag fails.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyB", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyB').id
        self.assertEqual(models.FAILURE, self.tags.add_tag(card_id, ""))

    def testAddTagNone(self):
        """
        Tests that adding a None tag fails.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyC", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyC').id
        self.assertEqual(models.FAILURE, self.tags.add_tag(card_id, None))

    def testAddCardIDEmpty(self):
        """
        Tests that adding a tag to an empty card ID fails.
        """
        self.assertEqual(models.FAILURE, self.tags.add_tag("", "tech"))

    def testAddCardIDNone(self):
        """
        Tests that adding a tag to a None card ID fails.
        """
        self.assertEqual(models.FAILURE, self.tags.add_tag(None, "tech"))

    def testAddCardIDNonexistent(self):
        """
        Tests that adding a tag to a card that doesn't exist fails.
        """
        self.assertEqual(models.FAILURE, self.tags.add_tag(models.Card.objects.get(name='THIS_CARD_DOESNT_EXIST').id,
                                                           "tech"))

    ##################
    ##              ##
    ##  MODIFY TAG  ##
    ##              ##
    ##################

    def testModifyTag(self):
        """
        Tests that modifying a card's tag with a new tag between 1-128 characters succeeds.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyD", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyD').id
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "tech"))
        self.assertEqual(models.SUCCESS, self.tags.modify_tag(card_id, "tech", "engineer"))

    def testModifyTagLong1(self):
        """
        Tests that modifying a card's tag with a new tag that exceeds 128 characters fails.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyE", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyE').id
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "tech"))
        new_long_tag = "superlongtagahhhhhh"*10
        self.assertEqual(models.FAILURE, self.tags.modify_tag(card_id, "tech", new_long_tag))

    def testModifyTagLong2(self):
        """
        Tests that passing in a current_tag_name that is over 128 characters fails.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyF", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyF').id
        long_current_tag = "superlongtagahhhhhh"*10
        self.assertEqual(models.FAILURE, self.tags.modify_tag(card_id, long_current_tag, "shorter_tag"))

    def testModifyTagNonexistentCard(self):
        """
        Tests that modifying a tag on a card that doesn't exist fails.
        """
        self.assertEqual(models.FAILURE, self.tags.modify_tag(models.Card.objects.get(name='NONEXISTENT_COMPANY').id,
                                                              "hardware", "software"))

    def testModifyTagNonexistent(self):
        """
        Tests that passing in a current_tag_name that doesn't exist fails.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyG", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyG').id
        self.assertEqual(models.FAILURE, self.tags.modify_tag(card_id, "this_tag_doesnt_exist", "new_tag"))

    def testModifyTagDuplicate(self):
        """
        Tests that modifying a tag to one that already exists will fail.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyH", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyH').id
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "tech"))
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "engineer"))
        self.assertEqual(models.FAILURE, self.tags.modify_tag(card_id, "tech", "engineer"))

    ################
    ##            ##
    ##  GET TAGS  ##
    ##            ##
    ################

    def testGetTags(self):
        """
        Tests that it returns a list of tags associated with an existing card_id.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyI", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyI').id
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "tech"))
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "software"))
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "engineer"))
        tags_list = ["tech", "software", "engineer"]
        self.assertEqual(tags_list, self.tags.get_tags(card_id))

    def testGetTagsInvalidCard(self):
        """
        Tests that it doesn't return a list of tags for a non-existent card id.
        """
        self.assertEqual(models.FAILURE, self.tags.get_tags("THIS_CARD_ID_DOESNT_EXIST"))

    ###################
    ##               ##
    ##  REMOVE TAGS  ##
    ##               ##
    ###################

    def testRemoveTagInvalidCard(self):
        """
        Tests that it fails to removes an existing tag from a non-existent card.
        """
        self.assertEqual(models.FAILURE, self.tags.remove_tag("THIS_CARD_ID_DOESNT_EXIST", "tech"))

    def testRemoveTagNonexistentTag(self):
        """
        Tests that it fails to removes a non-existent tag from an existing card.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyJ", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyJ').id
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "software"))
        self.assertEqual(models.FAILURE, self.tags.remove_tag(card_id, "hardware"))

    def testRemoveTag(self):
        """
        Tests that it successfully removes an existing tag from an existing card.
        """
        self.assertEqual(models.SUCCESS, self.tags.create_card("CompanyK", "Software Engineer", 2))
        card_id = models.Card.objects.get(name='CompanyK').id
        self.assertEqual(models.SUCCESS, self.tags.add_tag(card_id, "tech"))
        self.assertEqual(models.SUCCESS, self.tags.remove_tag(card_id, "tech"))

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
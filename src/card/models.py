from django.db import models
import uuid

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default="")

class Deck(models.Model):
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
<<<<<<< HEAD
    associated_company = models.OneToOneField(Company)
    owner = models.ForeignKey('user.UserProfile')


    def __str__(self):
        return "A card for " + self.status

#Position
class Card(models.Model): 
    card_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    job_title = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=20, blank=False, default="Interested")
    notes = models.TextField(default="")
    card_deck = models.ForeignKey(Deck)



=======
    status = models.CharField(max_length=20, blank=False, default="Interested")
    job_title = models.CharField(max_length=255, blank=False)
    associated_company = models.ForeignKey(Company)
    notes = models.TextField(default="")
    owner = models.ForeignKey('user.UserProfile')

    def __str__(self):
        return "A card for " + self.status
>>>>>>> 2af7208e384aaf04ca959db7c1e0ae0d37a15dde

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    tagged_card = models.ForeignKey(Card)

    def __str__(self):
        return self.tag

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    associated_card = models.ForeignKey(Card)

    def __str__(self):
        return "Contact with name " + self.name

class Task(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=20, blank=False, default="incomplete")
    associated_card = models.ForeignKey(Card)

    def __str__(self):
<<<<<<< HEAD
        return "Tasks for " + self.associated_card.name
=======
        return "Tasks for " + self.associated_card.name
>>>>>>> 2af7208e384aaf04ca959db7c1e0ae0d37a15dde

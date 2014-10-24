from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from user.models import *
from document.models import *

class Company(models.Model):
    name = models.CharField(unique=True)
    # Maybe
    # description = models.TextField()

class Card(models.Model):
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    status = models.CharField(max_length=20, blank=False, default="begin interviewing")
    job_title = models.CharField(blank=False)
    associated_company = models.ForeignKey(Company)

    def __str__(self):
        return "A card for " + associated_company

class Tag(models.Model):
    tag = models.CharField(unique=True)
    tagged_card = models.ForeignKey(Card)

    def __str__(self):
        return tag

class Contact(models.Model):
    name = models.CharField(blank=False)
    phone = models.CharField(blank=False)
    email = models.EmailField()
    associated_card = models.ForeignKey(Card)

    def __str__(self):
        return "Contact with name " + name


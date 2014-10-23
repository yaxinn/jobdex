from django.db import models
import uuid

class Card(models.Model):
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
# Could be a different model if we want to later store additional info per company
    associated_company = models.CharField()

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
    date = models.DateField(blank=False)
    associated_card = models.ForeignKey(Card)

    def __str__(self):
        return "Contact with name " + name

from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
from user.models import *
from card.models import *

# Create your models here.
class Document(models.Model):
	doc_name = models.CharField(max_length=255)
	date_uploaded = models.DateTimeField(default=datetime.now())
	pdf=models.FileField(upload_to='documents/', blank=True, null=True)
	uploaded_by=models.ForeignKey('user')
	def __str__(self):
		return self.doc_name


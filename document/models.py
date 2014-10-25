from django.db import models
import uuid
from datetime import datetime
import user

class Document(models.Model):
    doc_name = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(default=datetime.now())
    pdf = models.FileField(upload_to='documents/', blank=True, null=True)
    uploaded_by = models.ForeignKey(user.models.UserProfile)
    def __str__(self):
        return self.doc_name

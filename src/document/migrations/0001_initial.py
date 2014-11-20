# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unique_id', models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True)),
                ('doc_name', models.CharField(unique=True, max_length=255)),
                ('date_uploaded', models.DateTimeField(default=datetime.datetime(2014, 11, 20, 21, 18, 23, 169596))),
                ('pdf', models.FileField(null=True, upload_to=b'documents/', blank=True)),
                ('uploaded_by', models.ForeignKey(to='user.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_name', models.CharField(max_length=255)),
                ('date_uploaded', models.DateTimeField(default=datetime.datetime(2014, 10, 25, 0, 5, 33, 962803))),
                ('pdf', models.FileField(null=True, upload_to=b'documents/', blank=True)),
                ('uploaded_by', models.ForeignKey(to='user.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20141025_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='unique_id',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 6, 35, 28, 234969)),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]

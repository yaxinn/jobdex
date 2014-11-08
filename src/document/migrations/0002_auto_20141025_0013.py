# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 25, 0, 13, 28, 378688)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20141025_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 7, 0, 10, 928264)),
        ),
    ]

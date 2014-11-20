# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20141120_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 20, 22, 45, 46, 962191)),
        ),
    ]

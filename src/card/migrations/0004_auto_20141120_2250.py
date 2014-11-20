# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20141120_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='job_title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(default=b'Interested', max_length=20, blank=True),
        ),
    ]

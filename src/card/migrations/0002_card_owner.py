# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.ForeignKey(to='user.UserProfile'),
            preserve_default=True,
        ),
    ]

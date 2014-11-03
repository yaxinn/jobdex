# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20141025_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.CharField(max_length=100)),
                ('status', models.CharField(default=b'incomplete', max_length=20)),
                ('associated_card', models.ForeignKey(to='card.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='notes',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]

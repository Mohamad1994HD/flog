# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-19 07:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 4, 19, 7, 50, 2, 919732, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
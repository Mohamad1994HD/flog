# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170424_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
    ]
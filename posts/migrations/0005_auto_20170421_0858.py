# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-21 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]

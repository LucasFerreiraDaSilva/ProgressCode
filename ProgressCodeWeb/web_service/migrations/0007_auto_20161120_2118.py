# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-20 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_service', '0006_auto_20161120_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]

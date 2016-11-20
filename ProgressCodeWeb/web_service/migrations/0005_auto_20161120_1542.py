# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-20 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_service', '0004_auto_20161119_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='observacao',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='senha',
        ),
        migrations.AddField(
            model_name='tutor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutor',
            name='joined',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='password',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
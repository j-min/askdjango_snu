# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20170411_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intent',
            name='title',
            field=models.CharField(blank=True, choices=[('yesintent', 'yesintent'), ('nointent', 'nointent'), ('letschatintent', 'letschatintent'), ('chatintent', 'chatintent')], max_length=100),
        ),
    ]

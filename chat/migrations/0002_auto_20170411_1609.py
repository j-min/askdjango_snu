# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='conversation_id',
        ),
        migrations.RemoveField(
            model_name='session',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='intent',
            name='intent_id',
        ),
        migrations.RemoveField(
            model_name='query',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='response',
            name='reponse_id',
        ),
        migrations.RemoveField(
            model_name='response',
            name='session_id',
        ),
        migrations.AlterField(
            model_name='query',
            name='correctly_responded',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]

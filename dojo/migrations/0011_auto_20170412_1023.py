# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0010_auto_20170412_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.Reporter', verbose_name='기자'),
        ),
    ]

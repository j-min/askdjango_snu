# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0004_auto_20170412_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, choices=[('science', '과학'), ('economy', '경제'), ('politics', '정치'), ('sports', '스포츠')], default='과학', max_length=100),
        ),
    ]

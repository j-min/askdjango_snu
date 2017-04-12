# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import dojo.models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0005_auto_20170412_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='경도, 위도 포맷으로 입력', max_length=50, validators=[dojo.models.lnglat_validator]),
        ),
    ]

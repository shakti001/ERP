# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-19 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_auto_20180218_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='occupancy',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='space',
            name='areas',
            field=models.CharField(max_length=50000),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0030_productmetalist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmetalist',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProductMetaList',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-29 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientRelationships', '0007_deal_dueperiod'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='grandTotal',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20180329_0831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='name',
            new_name='jobtype',
        ),
    ]
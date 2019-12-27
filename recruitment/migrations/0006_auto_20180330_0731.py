# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 07:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruitment', '0005_auto_20180329_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='contact',
        ),
        migrations.AddField(
            model_name='jobs',
            name='contacts',
            field=models.ManyToManyField(related_name='jobHeading', to=settings.AUTH_USER_MODEL),
        ),
    ]

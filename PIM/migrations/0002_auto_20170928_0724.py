# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PIM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='eventType',
            field=models.CharField(choices=[(b'Meeting', b'Meeting'), (b'Reminder', b'Reminder'), (b'ToDo', b'ToDo'), (b'EVENT', b'EVENT'), (b'Deadline', b'Deadline'), (b'Other', b'Other')], default=b'Other', max_length=11),
        ),
    ]

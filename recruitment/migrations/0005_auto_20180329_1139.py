# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0004_auto_20180329_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='jobtype',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Contract', 'Contract'), ('Intern', 'Intern')], default='Intern', max_length=15),
        ),
    ]

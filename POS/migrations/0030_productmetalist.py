# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 10:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('POS', '0029_productverient'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMetaList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=10000, null=True)),
                ('code', models.PositiveIntegerField(default=0)),
                ('taxRate', models.PositiveIntegerField(default=0)),
                ('hsn', models.BooleanField(default=True)),
                ('sac', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productMetaList', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 03:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('hra', models.PositiveIntegerField(null=True)),
                ('special', models.PositiveIntegerField(null=True)),
                ('lta', models.PositiveIntegerField(null=True)),
                ('basic', models.PositiveIntegerField(null=True)),
                ('adHoc', models.PositiveIntegerField(null=True)),
                ('policyNumber', models.PositiveIntegerField(null=True)),
                ('provider', models.PositiveIntegerField(null=True)),
                ('amount', models.PositiveIntegerField(null=True)),
                ('noticePeriodRecovery', models.FloatField()),
                ('al', models.PositiveIntegerField(null=True)),
                ('ml', models.PositiveIntegerField(null=True)),
                ('adHocLeaves', models.PositiveIntegerField(null=True)),
                ('joiningDate', models.DateField(auto_now=True)),
                ('off', models.FloatField()),
                ('accountNumber', models.PositiveIntegerField(null=True)),
                ('ifscCode', models.PositiveIntegerField(null=True)),
                ('bankDetais', models.PositiveIntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 17:58
from __future__ import unicode_literals

import HR.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='accountsKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(blank=True, max_length=40)),
                ('key_expires', models.DateTimeField(default=django.utils.timezone.now)),
                ('keyType', models.CharField(choices=[(b'hashed', b'hashed'), (b'otp', b'otp')], default=b'hashed', max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountKey', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitType', models.CharField(choices=[(b'Not selected..', b'Not selected..'), (b'Research and Development', b'Research and Development'), (b'Operations', b'Operations'), (b'Management', b'Management')], default=b'Not selected..', max_length=30)),
                ('domain', models.CharField(choices=[(b'Not selected..', b'Not selected..'), (b'Automotive', b'Automotive'), (b'Service', b'Service'), (b'University', b'University'), (b'FMCG', b'FMCG'), (b'Power', b'Power'), (b'Pharmaceuticals', b'Pharmaceuticals'), (b'Manufacturing', b'Manufacturing'), (b'Tele Communications', b'Tele Communications')], default=b'Not selected..', max_length=15)),
                ('unit', models.CharField(max_length=30, null=True)),
                ('department', models.CharField(max_length=30, null=True)),
                ('primaryApprover', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approving', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=400)),
                ('issuedTo', models.CharField(max_length=400)),
                ('passKey', models.CharField(max_length=4)),
                ('email', models.CharField(max_length=35)),
                ('docID', models.CharField(blank=True, max_length=10)),
                ('app', models.CharField(blank=True, max_length=20)),
                ('issuedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificatesIssued', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empID', models.PositiveIntegerField(null=True, unique=True)),
                ('displayPicture', models.ImageField(upload_to=HR.models.getDisplayPicturePath)),
                ('dateOfBirth', models.DateField(null=True)),
                ('anivarsary', models.DateField(null=True)),
                ('permanentAddressStreet', models.TextField(blank=True, max_length=100, null=True)),
                ('permanentAddressCity', models.CharField(blank=True, max_length=15, null=True)),
                ('permanentAddressPin', models.IntegerField(blank=True, null=True)),
                ('permanentAddressState', models.CharField(blank=True, max_length=20, null=True)),
                ('permanentAddressCountry', models.CharField(blank=True, max_length=20, null=True)),
                ('localAddressStreet', models.TextField(max_length=100, null=True)),
                ('localAddressCity', models.CharField(max_length=15, null=True)),
                ('localAddressPin', models.IntegerField(null=True)),
                ('localAddressState', models.CharField(max_length=20, null=True)),
                ('localAddressCountry', models.CharField(max_length=20, null=True)),
                ('prefix', models.CharField(choices=[(b'NA', b'NA'), (b'Mr', b'Mr'), (b'Mrs', b'Mrs'), (b'Smt', b'Smt'), (b'Shri', b'Shri')], default=b'NA', max_length=4)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')], default=b'M', max_length=6)),
                ('email', models.EmailField(max_length=50)),
                ('email2', models.EmailField(blank=True, max_length=50)),
                ('mobile', models.CharField(max_length=14, null=True)),
                ('emergency', models.PositiveIntegerField(null=True)),
                ('tele', models.PositiveIntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=100, null=True)),
                ('sign', models.ImageField(null=True, upload_to=HR.models.getSignaturesPath)),
                ('IDPhoto', models.ImageField(null=True, upload_to=HR.models.getDisplayPicturePath)),
                ('TNCandBond', models.FileField(null=True, upload_to=HR.models.getTNCandBondPath)),
                ('resume', models.FileField(null=True, upload_to=HR.models.getResumePath)),
                ('certificates', models.FileField(null=True, upload_to=HR.models.getCertificatesPath)),
                ('transcripts', models.FileField(null=True, upload_to=HR.models.getTranscriptsPath)),
                ('otherDocs', models.FileField(blank=True, null=True, upload_to=HR.models.getOtherDocsPath)),
                ('almaMater', models.CharField(max_length=100, null=True)),
                ('pgUniversity', models.CharField(blank=True, max_length=100, null=True)),
                ('docUniversity', models.CharField(blank=True, max_length=100, null=True)),
                ('fathersName', models.CharField(max_length=100, null=True)),
                ('mothersName', models.CharField(max_length=100, null=True)),
                ('wifesName', models.CharField(blank=True, max_length=100, null=True)),
                ('childCSV', models.CharField(blank=True, max_length=100, null=True)),
                ('note1', models.TextField(blank=True, max_length=500, null=True)),
                ('note2', models.TextField(blank=True, max_length=500, null=True)),
                ('note3', models.TextField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(choices=[(b'management', b'management'), (b'rnd', b'rnd'), (b'operations', b'operations')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranksAuthored', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='designation',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HR.rank'),
        ),
        migrations.AddField(
            model_name='designation',
            name='reportingTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managing', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='designation',
            name='secondaryApprover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alsoApproving', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='designation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ecommerce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ERP', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='choiceLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='choiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='ecommerce.choiceLabel')),
            ],
        ),
        migrations.CreateModel(
            name='customerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendUpdates', models.BooleanField(default=True)),
                ('mobile', models.PositiveIntegerField(null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.address')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveIntegerField()),
                ('message', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldType', models.CharField(choices=[('char', 'char'), ('boolean', 'boolean'), ('float', 'float'), ('date', 'date'), ('choice', 'choice')], default='char', max_length=15)),
                ('unit', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('helpText', models.CharField(blank=True, max_length=100)),
                ('default', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='genericProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('minCost', models.PositiveIntegerField(default=0)),
                ('visual', models.ImageField(null=True, upload_to=ecommerce.models.getEcommerceProductVisualUploadPath)),
                ('fields', models.ManyToManyField(blank=True, related_name='products', to='ecommerce.field')),
            ],
        ),
        migrations.CreateModel(
            name='genericType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=2000)),
                ('priceModel', models.CharField(choices=[('quantity', 'quantity'), ('weight', 'weight'), ('time', 'time'), ('custom', 'custom')], default='quantity', max_length=15)),
                ('approved', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('product', 'product'), ('service', 'service')], default='service', max_length=15)),
                ('specifications', models.TextField(max_length=2000)),
                ('source', models.TextField(max_length=40000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('link', models.TextField(max_length=300, null=True)),
                ('attachment', models.FileField(null=True, upload_to=ecommerce.models.getEcommercePictureUploadPath)),
                ('mediaType', models.CharField(choices=[('onlineVideo', 'onlineVideo'), ('video', 'video'), ('image', 'image'), ('onlineImage', 'onlineImage'), ('doc', 'doc')], default='image', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecommerceMediaUploads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='offerBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('level', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to=ecommerce.models.getEcommerceBannerUploadPath)),
                ('title', models.CharField(max_length=20, null=True)),
                ('subtitle', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('params', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cod', models.BooleanField(default=False)),
                ('freeReturns', models.BooleanField(default=False)),
                ('replacementPeriod', models.PositiveIntegerField(null=True)),
                ('rate', models.PositiveIntegerField(null=True)),
                ('shippingOptions', models.CharField(choices=[('pickup', 'pickup'), ('homeDelivary', 'homeDelivary'), ('postal', 'postal')], default='pickup', max_length=15)),
                ('availability', models.CharField(choices=[('local', 'local'), ('state', 'state'), ('national', 'national'), ('international', 'international')], default='local', max_length=15)),
                ('shippingFee', models.PositiveIntegerField(null=True)),
                ('inStock', models.PositiveIntegerField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='providerOptions', to='ecommerce.listing')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offerings', to='ERP.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecommerceOfferings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paymentType', models.CharField(choices=[('onlineBanking', 'onlineBanking'), ('COD', 'COD'), ('eMoney', 'eMoney')], default='COD', max_length=15)),
                ('paid', models.BooleanField(default=False)),
                ('mobile', models.PositiveIntegerField(null=True)),
                ('shipping', models.CharField(max_length=20, null=True)),
                ('coupon', models.CharField(max_length=20, null=True)),
                ('rate', models.CharField(max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('inProgress', 'inProgress'), ('processing', 'processing'), ('acceptedByVendor', 'acceptedByVendor'), ('canceledByCustomer', 'canceledByCustomer'), ('canceledByVendor', 'canceledByVendor'), ('complete', 'complete')], default='new', max_length=20, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.address')),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecommerce.offering')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecommerceOrders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(null=True)),
                ('heading', models.CharField(max_length=75, null=True)),
                ('text', models.TextField(max_length=1000, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ecommerce.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='reviewLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('positive', models.BooleanField(default=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='ecommerce.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='saved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('cart', 'cart'), ('wishlist', 'wishlist')], default='cart', max_length=15)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inCarts', to='ecommerce.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecommerceCart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='files',
            field=models.ManyToManyField(related_name='listings', to='ecommerce.media'),
        ),
        migrations.AddField(
            model_name='listing',
            name='parentType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce.genericProduct'),
        ),
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecommerceListings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='genericproduct',
            name='productType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce.genericType'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='attachment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='ecommerce.media'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecommerceProfile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='offering',
            unique_together=set([('service', 'item')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=200)),
                ('eff_date', models.DateTimeField(blank=True, null=True)),
                ('exp_date', models.DateTimeField(blank=True, null=True)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=50)),
                ('license_no', models.CharField(max_length=20)),
                ('business_nature', models.CharField(max_length=20)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DIM_Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DIM_Contact_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=20)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DIM_GST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('percentage_claimable', models.DecimalField(decimal_places=2, max_digits=3)),
                ('percentage_chargeable', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DIM_Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('promo_cond', models.CharField(max_length=50)),
                ('promo_percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('promo_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DIM_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DIM_Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('dim_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.DIM_Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('eff_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('exp_datetime', models.DateTimeField()),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi_no', models.CharField(default='', max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doc_amt', models.DecimalField(decimal_places=2, max_digits=7)),
                ('doc_gst_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('doc_promotion_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('remark', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=1)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('gst_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('det_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Inventory')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.DIM_Promotion')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('si_no', models.CharField(default='', max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('sales_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doc_amt', models.DecimalField(decimal_places=2, max_digits=7)),
                ('doc_gst_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('doc_promotion_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('remark', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=20)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saless', to='retail.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=1)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('gst_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('det_amt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Inventory')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.DIM_Promotion')),
                ('sales', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='retail.Sales')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=50)),
                ('license_no', models.CharField(max_length=20)),
                ('business_nature', models.CharField(max_length=20)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('eff_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('exp_datetime', models.DateTimeField()),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.DIM_GST')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Inventory')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Supplier'),
        ),
        migrations.AddField(
            model_name='dim_promotion',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.Inventory'),
        ),
        migrations.AddField(
            model_name='dim_access',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retail.DIM_Role'),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='contacttype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retail.DIM_Contact_Type'),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0010_auto_20170116_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address1',
            new_name='bill_address1',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='address2',
            new_name='bill_address2',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='address3',
            new_name='bill_address3',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='city',
            new_name='bill_city',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='postcode',
            new_name='bill_postcode',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='state',
            new_name='bill_state',
        ),
        migrations.AddField(
            model_name='customer',
            name='ship_address1',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='ship_address2',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='ship_address3',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='ship_city',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='ship_postcode',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]

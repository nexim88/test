# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-11 01:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0014_sales_det_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

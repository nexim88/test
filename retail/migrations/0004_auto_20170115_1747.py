# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0003_remove_sales_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sales_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0020_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_det',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='retail.DIM_Promotion'),
        ),
    ]

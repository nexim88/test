# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0013_sales_det_net_amt'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_det',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]

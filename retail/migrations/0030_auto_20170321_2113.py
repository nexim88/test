# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0029_auto_20170321_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='imgFile',
            field=models.FileField(upload_to='documents/'),
        ),
    ]

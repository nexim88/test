# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0024_webtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtemplate',
            name='pageSectionimgFile',
            field=models.FileField(blank=True, null=True, upload_to='documents/Template/'),
        ),
        migrations.AlterField(
            model_name='webtemplate',
            name='pageURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
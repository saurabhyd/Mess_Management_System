# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0005_auto_20171101_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='messadmin',
            name='lname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messmenu', '0002_auto_20171011_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='sno',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

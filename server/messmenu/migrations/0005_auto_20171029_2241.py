# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messmenu', '0004_auto_20171029_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='sno',
            new_name='s1',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messmenu', '0003_menu_sno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='sno',
            field=models.PositiveIntegerField(),
        ),
    ]

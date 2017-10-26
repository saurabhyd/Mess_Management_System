# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=15)),
                ('food', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mess',
            fields=[
                ('messbno', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=15)),
                ('region', models.CharField(max_length=15)),
                ('vacancy', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='messbno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messmenu.mess'),
        ),
    ]
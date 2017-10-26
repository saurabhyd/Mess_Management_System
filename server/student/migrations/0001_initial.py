# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='messreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messbno', models.PositiveIntegerField()),
                ('validity', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('usn', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('messrno', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('bno', models.PositiveIntegerField()),
                ('branch', models.CharField(max_length=50)),
                ('sem', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='messreg',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student_details'),
        ),
    ]

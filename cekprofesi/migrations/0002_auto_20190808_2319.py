# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-08 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cekprofesi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matkul',
            name='id',
        ),
        migrations.RemoveField(
            model_name='matkur',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profesi',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profesi_matkul',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profesi_matkur',
            name='id',
        ),
        migrations.AlterField(
            model_name='matkul',
            name='kdmk',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='matkur',
            name='kdmkr',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesi',
            name='kdprofesi',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesi_matkul',
            name='profesi',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesi_matkur',
            name='profesi',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-15 03:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cekprofesi', '0002_auto_20190808_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matkul',
            name='sks',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-17 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cekprofesi', '0008_auto_20190817_0352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesi_matkul',
            old_name='kdmatkul',
            new_name='kdmk',
        ),
        migrations.AlterField(
            model_name='matkul',
            name='matkul',
            field=models.CharField(max_length=9),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-18 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cekprofesi', '0010_auto_20190817_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesi_matkul',
            name='kdmk',
        ),
        migrations.AddField(
            model_name='profesi_matkul',
            name='kdmk',
            field=models.ManyToManyField(default='', to='cekprofesi.Matkul'),
        ),
    ]

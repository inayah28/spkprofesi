# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-16 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cekprofesi', '0006_auto_20190817_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesi_matkul',
            name='kdmk',
        ),
        migrations.AddField(
            model_name='profesi_matkul',
            name='matkul',
            field=models.ManyToManyField(to='cekprofesi.Matkul'),
        ),
    ]
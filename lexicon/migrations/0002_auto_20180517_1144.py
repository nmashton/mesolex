# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lexicalentry',
            name='headword',
            field=models.CharField(db_index=True, max_length=256, verbose_name='Headword'),
        ),
    ]

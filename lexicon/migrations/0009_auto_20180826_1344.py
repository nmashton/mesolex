# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-26 13:44
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0008_auto_20180825_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grammargroup',
            name='inflectional_type',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='grammargroup',
            name='misc_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grammargroup',
            name='part_of_speech',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
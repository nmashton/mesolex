# Generated by Django 3.0.7 on 2020-12-13 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0014_entry_longsearchablestring_searchablestring'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='entry',
        ),
        migrations.AddField(
            model_name='media',
            name='lexical_entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lexicon.Entry'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-24 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pandion', '0004_observations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Observations',
            new_name='Observation',
        ),
    ]

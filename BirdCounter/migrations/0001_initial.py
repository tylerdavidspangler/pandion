# Generated by Django 4.0.2 on 2022-09-23 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EW_Bird',
            fields=[
                ('name', models.CharField(max_length=1000, unique=True)),
                ('id', models.CharField(max_length=1000, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(max_length=1000)),
            ],
        ),
    ]

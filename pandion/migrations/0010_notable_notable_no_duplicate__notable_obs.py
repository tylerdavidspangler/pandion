# Generated by Django 4.0.2 on 2022-03-03 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandion', '0009_bird_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciesCode', models.CharField(max_length=100)),
                ('comName', models.CharField(max_length=100)),
                ('locId', models.CharField(max_length=100)),
                ('locName', models.CharField(max_length=100)),
                ('obsDt', models.CharField(max_length=100)),
                ('howMany', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('mod_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddConstraint(
            model_name='notable',
            constraint=models.UniqueConstraint(fields=('speciesCode', 'obsDt', 'locId'), name='no_duplicate__notable_obs'),
        ),
    ]

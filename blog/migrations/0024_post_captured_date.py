# Generated by Django 4.0.2 on 2022-04-08 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='captured_Date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
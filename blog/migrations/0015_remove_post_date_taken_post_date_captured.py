# Generated by Django 4.0.2 on 2022-04-08 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_date_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_Taken',
        ),
        migrations.AddField(
            model_name='post',
            name='date_Captured',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

# Generated by Django 4.0.2 on 2022-04-08 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_title_remove_post_updated_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Taken',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

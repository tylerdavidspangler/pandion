# Generated by Django 4.0.2 on 2022-04-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_post_city_remove_post_photo_specs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_Captured',
            new_name='captured',
        ),
    ]
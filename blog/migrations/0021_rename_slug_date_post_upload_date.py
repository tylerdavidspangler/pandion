# Generated by Django 4.0.2 on 2022-04-08 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_post_slug_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug_Date',
            new_name='upload_Date',
        ),
    ]
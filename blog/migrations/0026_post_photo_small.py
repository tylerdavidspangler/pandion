# Generated by Django 4.0.2 on 2022-04-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_post_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_Small',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]

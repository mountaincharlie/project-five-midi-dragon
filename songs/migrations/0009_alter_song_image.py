# Generated by Django 3.2 on 2022-08-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.jpg', null=True, upload_to=''),
        ),
    ]

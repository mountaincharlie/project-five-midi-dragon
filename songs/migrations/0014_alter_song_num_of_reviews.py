# Generated by Django 3.2 on 2022-08-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0013_song_num_of_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='num_of_reviews',
            field=models.CharField(blank=True, default='N/A', max_length=4, null=True),
        ),
    ]
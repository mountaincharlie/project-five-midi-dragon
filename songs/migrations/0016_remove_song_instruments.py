# Generated by Django 3.2 on 2022-08-21 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0015_songinstrument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='instruments',
        ),
    ]

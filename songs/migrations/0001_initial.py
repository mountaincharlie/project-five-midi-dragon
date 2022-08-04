# Generated by Django 3.2 on 2022-08-04 16:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260, unique=True)),
                ('display_name', models.CharField(max_length=260, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260, unique=True)),
                ('display_name', models.CharField(max_length=260, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260, unique=True)),
                ('song_length_range', models.CharField(max_length=100)),
                ('num_included_instruments', models.PositiveIntegerField()),
                ('num_included_reviews', models.PositiveIntegerField()),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'ordering': ['min_price'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260)),
                ('image', models.ImageField(blank=True, default='placeholder.jpg', null=True, upload_to='')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
                ('bpm', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(35), django.core.validators.MaxValueValidator(155)])),
                ('duration', models.DurationField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('song_purpose', models.TextField(blank=True, null=True)),
                ('song_feel', models.TextField(blank=True, null=True)),
                ('additional_details', models.TextField(blank=True, null=True)),
                ('use_as_testinomial', models.BooleanField(default=False)),
                ('testimonial_text', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.genre')),
                ('instruments', models.ManyToManyField(blank=True, related_name='song_instrument', to='songs.Instrument')),
                ('likes', models.ManyToManyField(blank=True, related_name='song_like', to=settings.AUTH_USER_MODEL)),
                ('project_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.projecttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]

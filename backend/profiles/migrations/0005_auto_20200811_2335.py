# Generated by Django 3.0.1 on 2020-08-12 03:35

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200810_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followed',
            field=models.ManyToManyField(blank=True, related_name='followers', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=profiles.models.profile_directory_path, verbose_name='profile picture'),
        ),
    ]

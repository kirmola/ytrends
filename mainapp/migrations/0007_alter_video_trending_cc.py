# Generated by Django 5.0.4 on 2024-04-16 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_video_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='trending_cc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.country', to_field='country_code', verbose_name='Trending CC'),
        ),
    ]

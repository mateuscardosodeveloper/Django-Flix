# Generated by Django 3.2.8 on 2021-10-12 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_rename_timestamp_video_created_at'),
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.video'),
        ),
    ]

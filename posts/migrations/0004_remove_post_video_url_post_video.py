# Generated by Django 5.1.3 on 2024-12-03 01:24

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video_url',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]

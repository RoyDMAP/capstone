# Generated by Django 5.1.3 on 2024-12-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

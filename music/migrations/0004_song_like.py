# Generated by Django 5.0.3 on 2024-05-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_song_options_alter_song_listened_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='like',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]

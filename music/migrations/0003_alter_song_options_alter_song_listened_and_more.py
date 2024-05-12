# Generated by Django 5.0.3 on 2024-05-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_listened'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='song',
            name='listened',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='song',
            index=models.Index(fields=['id'], name='music_song_id_82e124_idx'),
        ),
    ]

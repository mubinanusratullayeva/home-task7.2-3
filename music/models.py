from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=70)
    image = models.URLField()
    like = models.PositiveBigIntegerField(default=0)
    last_updated = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=70)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.URLField()
    last_updated = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


class Song(models.Model):
    title = models.CharField(max_length=70)
    cover = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    listened = models.PositiveBigIntegerField(default=0)
    like = models.PositiveBigIntegerField(default=0)
    last_updated = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

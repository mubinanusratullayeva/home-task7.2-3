from rest_framework import serializers

from .models import Artist, Album, Song


class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'image')


class AlbumsSerializer(serializers.ModelSerializer):
    artist = ArtistsSerializer()

    class Meta:
        model = Album
        fields = ('title', 'cover', 'artist')


class SongsSerializer(serializers.ModelSerializer):
    album = AlbumsSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ('title', 'cover', 'album', 'listened', 'like')

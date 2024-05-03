from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Artist, Album, Song
from .serializers import ArtistsSerializer, AlbumsSerializer, SongsSerializer


# Create your views here.
class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hi lazy developer"})


class ArtistsAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistsSerializer(artists, many=True)

        return Response(data=serializer.data)


class ArtistsDetailAPIView(APIView):
    def get(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistsSerializer(artist)

        return Response(data=serializer.data)


class AlbumsAPIView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumsSerializer(albums, many=True)

        return Response(data=serializer.data)


class AlbumsDetailAPIView(APIView):
    def get(self, request, id):
        album = Album.objects.get(id=id)
        serializer = AlbumsSerializer(album)

        return Response(data=serializer.data)


class SongsAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongsSerializer(songs, many=True)

        return Response(data=serializer.data)


class SongsDetailAPIView(APIView):
    def get(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongsSerializer(song)

        return Response(data=serializer.data)

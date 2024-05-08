from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Artist, Album, Song
from .serializers import ArtistsSerializer, AlbumsSerializer, SongsSerializer


# Create your views here.
class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hi lazy developer"})


class ArtistsAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
    # permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


# class ArtistsAPIView(APIView):
#     def get(self, request):
#         artists = Artist.objects.all()
#         serializer = ArtistsSerializer(artists, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ArtistsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArtistsDetailAPIView(APIView):
#     def get(self, request, id):
#         try:
#             artist = Artist.objects.get(id=id)
#             serializer = ArtistsSerializer(artist)
#
#             return Response(data=serializer.data)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def patch(self, request, id):
#         artist = Artist.objects.get(id=id)
#         serializer = ArtistsSerializer(instance=artist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, id):
#         artist = Artist.objects.get(id=id)
#         serializer = ArtistsSerializer(instance=artist, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         artist = Artist.objetcs.get(id=id)
#         artist.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class AlbumsAPIView(APIView):
#     def get(self, request):
#         albums = Album.objects.all()
#         serializer = AlbumsSerializer(albums, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = AlbumsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumsAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


# class AlbumsDetailAPIView(APIView):
#     def get(self, request, id):
#         try:
#             album = Album.objects.get(id=id)
#             serializer = AlbumsSerializer(album)
#
#             return Response(data=serializer.data)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def patch(self, request, id):
#         album = Album.objects.get(id=id)
#         serializer = AlbumsSerializer(instance=album, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, id):
#         album = Album.objects.get(id=id)
#         serializer = AlbumsSerializer(instance=album, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         album = Album.objetcs.get(id=id)
#         album.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)


class SongsAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

from django.urls import path

from .views import (
    LandingPageAPIView,
    ArtistsAPIView,
    ArtistsDetailAPIView,
    AlbumsAPIView,
    AlbumsDetailAPIView,
    SongsAPIView,
    SongsDetailAPIView
)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path('artists/', ArtistsAPIView.as_view(), name="artists"),
    path('artists/<int:id>/', ArtistsDetailAPIView.as_view(), name="artist-detail"),
    path('albums/', AlbumsAPIView.as_view(), name="albums"),
    path('albums/<int:id>/', AlbumsDetailAPIView.as_view(), name="album-detail"),
    path('songs/', SongsAPIView.as_view(), name="songs"),
    path('songs/<int:id>/', SongsDetailAPIView.as_view(), name="song-detail"),
]

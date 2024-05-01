from django.urls import path

from .views import LandingPageAPIView, ArtistsAPIView, AlbumsAPIView, SongsAPIView

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path('artists/', ArtistsAPIView.as_view(), name="artists"),
    path('albums/', AlbumsAPIView.as_view(), name="albums"),
    path('songs/', SongsAPIView.as_view(), name="songs"),
]

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    LandingPageAPIView,
    ArtistsAPIView,
    ArtistsDetailAPIView,
    AlbumsAPIView,
    AlbumsDetailAPIView,
    SongsAPIViewSet
)


routers = DefaultRouter()
routers.register("songs", viewset=SongsAPIViewSet)


urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path('artists/', ArtistsAPIView.as_view(), name="artists"),
    path('artists/<int:id>/', ArtistsDetailAPIView.as_view(), name="artist-detail"),
    path('albums/', AlbumsAPIView.as_view(), name="albums"),
    path('albums/<int:id>/', AlbumsDetailAPIView.as_view(), name="album-detail"),
    path('', include(routers.urls))
]

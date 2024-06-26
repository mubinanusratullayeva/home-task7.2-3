from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import (
    LandingPageAPIView,
    # ArtistsAPIView,
    # ArtistsDetailAPIView,
    # AlbumsAPIView,
    # AlbumsDetailAPIView,
    SongsAPIViewSet,
    AlbumsAPIViewSet,
    ArtistsAPIViewSet
)


routers = DefaultRouter()
routers.register("songs", viewset=SongsAPIViewSet)
routers.register("albums", viewset=AlbumsAPIViewSet)
routers.register("artists", viewset=ArtistsAPIViewSet)


urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    # path('artists/', ArtistsAPIView.as_view(), name="artists"),
    # path('artists/<int:id>/', ArtistsDetailAPIView.as_view(), name="artist-detail"),
    # path('albums/', AlbumsAPIView.as_view(), name="albums"),
    # path('albums/<int:id>/', AlbumsDetailAPIView.as_view(), name="album-detail"),
    path('', include(routers.urls)),
    path('auth/', views.obtain_auth_token)
]

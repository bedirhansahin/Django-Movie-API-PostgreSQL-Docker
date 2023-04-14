from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r'genres', views.GenreView, basename='genres')
router.register(r'directors', views.DirectorView, basename='directors')

app_name = 'movie'

urlpatterns = router.urls

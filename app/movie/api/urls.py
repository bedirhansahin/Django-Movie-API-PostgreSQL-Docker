from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'genres', views.GenreView, basename='genres')

app_name = 'movie'

urlpatterns = router.urls

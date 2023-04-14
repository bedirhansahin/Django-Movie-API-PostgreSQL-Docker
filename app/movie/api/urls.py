from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r'genres', views.GenreView, basename='genres')
router.register(r'directors', views.DirectorView, basename='directors')

app_name = 'movie'

urlpatterns = router.urls

urlpatterns += [
    path('movies', views.MovieListView.as_view(), name='movies'),
    path('movies/<uuid:movie_id>', views.MovieRetrieveView.as_view(), name='movie-detail'),
]

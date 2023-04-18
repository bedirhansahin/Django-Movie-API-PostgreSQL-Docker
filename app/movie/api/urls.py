from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r'genres', views.GenreView, basename='genres')
router.register(r'directors', views.DirectorView, basename='directors')

app_name = 'movie'

urlpatterns = router.urls

urlpatterns += [
    path('movie/list', views.MovieListView.as_view(), name='movie-list'),
    path('movie/<uuid:movie_id>', views.MovieRetrieveView.as_view(), name='movie-detail'),
    path('movie/create', views.MovieCreateView.as_view(), name='movie-create'),
    path('comment/list', views.CommentAndScoreListAPIView.as_view(), name='comment-list'),
]

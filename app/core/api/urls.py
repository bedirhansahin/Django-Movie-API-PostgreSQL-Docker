from django.urls import path

from .views import (
    UserListAPIView,
    UserCreateAPIView,
    UserRetrieveAPIView,
)

app_name = 'core'

urlpatterns = [
    path('list', UserListAPIView.as_view(), name='user-list'),
    path('create', UserCreateAPIView.as_view(), name='user-create'),
    path('me', UserRetrieveAPIView.as_view(), name='user-me'),
]

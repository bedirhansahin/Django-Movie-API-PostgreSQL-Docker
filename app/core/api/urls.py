from django.urls import path

from .views import (
    UserListAPIView,
    UserCreateAPIView,
    UserRetrieveAPIView,
)

app_name = 'core'

urlpatterns = [
    path('user/list', UserListAPIView.as_view(), name='user-list'),
    path('user/create', UserCreateAPIView.as_view(), name='user-create'),
    path('user/me', UserRetrieveAPIView.as_view(), name='user-me'),
]

from django.urls import path

from .views import (
    UserListAPIView,
    UserCreateAPIView,
    UserRetrieveAPIView,
    CreateTokenAPIView
)

app_name = 'core'

urlpatterns = [
    path('users/list', UserListAPIView.as_view(), name='user-list'),
    path('users/create', UserCreateAPIView.as_view(), name='user-create'),
    path('users/me', UserRetrieveAPIView.as_view(), name='user-me'),
    path('token', CreateTokenAPIView.as_view(), name='token'),
]

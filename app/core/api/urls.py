from django.urls import path

from .views import (
    UserListAPIView,
    UserCreateAPIView,
    UserRetrieveAPIView,
    CreateTokenAPIView
)

app_name = 'core'

urlpatterns = [
    path('user/list', UserListAPIView.as_view(), name='user-list'),
    path('user/create', UserCreateAPIView.as_view(), name='user-create'),
    path('user/me', UserRetrieveAPIView.as_view(), name='user-me'),
    path('token', CreateTokenAPIView.as_view(), name='token'),
]

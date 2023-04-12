from django.urls import path

from .views import (
    UserListCreateAPIView,
    UserRetrieveAPIView
)

app_name = 'core'

urlpatterns = [
    path('user/list', UserListCreateAPIView.as_view(), name='user-list'),
    path('users/me', UserRetrieveAPIView.as_view(), name='user-me'),
]

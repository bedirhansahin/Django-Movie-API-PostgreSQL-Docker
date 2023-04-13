from django.urls import path

from .views import (
    UserListCreateAPIView,
    UserRetrieveAPIView
)

app_name = 'core'

urlpatterns = [
    path('users', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/me', UserRetrieveAPIView.as_view(), name='user-me'),
]

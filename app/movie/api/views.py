from rest_framework import (
    viewsets,
    mixins,
    generics,
    permissions,
    authentication,
    filters,
    status,
)
from rest_framework.exceptions import PermissionDenied

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django_filters import rest_framework as django_filters

from core.models import Genre, Director, Movie
from . serializers import (
    GenreSerializer,
)


class GenreView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Genre.objects.all().order_by('pk')
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_staff:
            raise PermissionDenied("You do not have permission to delete this object")
        self.perform_destroy(instance)
        return Response(
            {'detail': 'Object Deleted Successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("You do not have permission to create new object")
        return super().create(request, *args, **kwargs)




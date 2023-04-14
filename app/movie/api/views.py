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
from drf_spectacular.utils import (
    extend_schema,
)

from core.models import (
    Genre,
    Director,
    Movie)
from .serializers import (
    GenreSerializer,
    GenreCreateSerializer,
    DirectorSerializer,
    DirectorDetailSerializer,
    MovieSerializer,
    MovieDetailSerializer,
)


class GenreView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
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

    def get_serializer_class(self):
        if self.action == 'create':
            return GenreCreateSerializer
        return self.serializer_class


class DirectorView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Director.objects.all().order_by('pk')
    serializer_class = DirectorSerializer
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

    def retrieve(self, request, pk, *args, **kwargs):
        queryset = Director.objects.all()
        director = get_object_or_404(queryset, pk=pk)
        serializer = DirectorDetailSerializer(director)
        return Response(serializer.data)


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all().order_by('movie_name')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.BasicAuthentication]

    # Filter and Search
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['genre', 'director', 'country']
    ordering_fields = ['movie_name', 'imdb', 'production_year']
    search_fields = ['movie_name']


class MovieRetrieveView(generics.RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.BasicAuthentication]
    lookup_field = 'movie_id'

    def get_queryset(self):
        queryset = Movie.objects.filter(pk=self.kwargs['movie_id'])
        return queryset


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    @extend_schema(
        description='To  Select Country, You can Use General Country Code',
        responses={
            '201': MovieDetailSerializer,
            '400': 'Bad Request',
            '401': 'Unauthorized',
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)






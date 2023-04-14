from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from core.models import Genre, Director, Movie


# Genre's Movies serializer for director retrieve pages
class GenresMoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name']


class GenreSerializer(serializers.ModelSerializer):
    movies = GenresMoviesSerializer(many=True)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'movies']
        read_only_fields = ['movies']


class GenreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']


# Director's Movies serializer for director retrieve pages
class DirectorsMoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name']


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['id', 'name']


class DirectorDetailSerializer(DirectorSerializer):
    movies = DirectorsMoviesSerializer(many=True)

    class Meta(DirectorSerializer.Meta):
        fields = DirectorSerializer.Meta.fields + ['movies']
        read_only_fields = ['movies']


class MovieSerializer(
    CountryFieldMixin,
    serializers.ModelSerializer
):

    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name', 'director', 'genre', 'country', 'production_year', 'duration', 'imdb']
        read_only_fields = ['movie_id']


class MovieDetailSerializer(MovieSerializer):

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['story_line']

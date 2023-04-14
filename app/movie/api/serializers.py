from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from core.models import Genre, Director, Movie
from core.models_choices import SomeCountries


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


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

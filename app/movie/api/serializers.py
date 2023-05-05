from django.template.defaulttags import comment
from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from core.models import Genre, Director, Movie, CommentAndScore
from core.api.serializers import UserForCommentSerializer


# Genre's Movies serializer for director retrieve pages
class MoviesForCommentAndGenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name']


class GenreSerializer(serializers.ModelSerializer):
    movies = MoviesForCommentAndGenresSerializer(many=True)

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
    director = DirectorSerializer()

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['story_line']


class CommentAndScoreListSerializer(serializers.ModelSerializer):
    owner = UserForCommentSerializer(read_only=True)
    movie = MoviesForCommentAndGenresSerializer(read_only=True)

    class Meta:
        model = CommentAndScore
        fields = '__all__'


class CommentAndScoreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentAndScore
        fields = ['movie', 'comment', 'score']

    def save(self, *args, **kwargs):
        owner = self.context['request'].user
        comments = CommentAndScore(
            owner=owner,
            movie=self.validated_data['movie'],
            comment=self.validated_data['comment'],
            score=self.validated_data['score']
        )
        comments.save()
        return comments


class CommentAndScoreRetrieveSerializer(serializers.ModelSerializer):
    movie = MoviesForCommentAndGenresSerializer(read_only=True)

    class Meta:
        model = CommentAndScore
        fields = ['id', 'movie', 'comment', 'score']

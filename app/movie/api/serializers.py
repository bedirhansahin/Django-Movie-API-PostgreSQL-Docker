from rest_framework import serializers

from core.models import Genre, Director, Movie


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['id', 'name']

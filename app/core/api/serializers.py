from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Movie, Director, Genre


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'password2', 'is_active', 'gender', 'birth_date',]
        read_only_fields = ['is_active']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6, 'style': {'input_type': 'password'}},
            'password2': {'write_only': True, 'min_length': 6, 'style': {'input_type': 'password'}},
            'last_name': {'write_only': True},
            'email': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'Error': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'password2', 'birth_date', 'gender', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions']
        read_only_fields = ['groups', 'user_permissions', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6, 'style': {'input_type': 'password'}},
            'password2': {'write_only': True, 'min_length': 6, 'style': {'input_type': 'password'}},
        }
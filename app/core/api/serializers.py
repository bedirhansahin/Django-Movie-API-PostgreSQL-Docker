from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_active', 'gender', 'birth_date',]
        read_only_fields = ['is_active']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6, 'style': {'input_type': 'password'}},
            'last_name': {'write_only': True},
            'email': {'write_only': True},
        }

    def validate(self, data):
        return data


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'birth_date', 'gender', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions']
        read_only_fields = ['groups', 'user_permissions', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6, 'style': {'input_type': 'password'}},
        }

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return value

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for k, v in validated_data.items():
            setattr(instance, k, v)

        if password is not None:
            if len(password) < 6:
                raise serializers.ValidationError("Password must be at least 6 characters long.")

            instance.set_password(password)

        instance.save()

        return instance


class UserForCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100, style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            message = 'Authentication failed'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs



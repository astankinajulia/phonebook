import random
import string

from django.conf import settings
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator

from .models import User


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'email',
        )

    def create(self, validated_data):
        email = validated_data['email']
        validated_data['username'] = email.split('@')[0]
        return User.objects.create(**validated_data)


class TokenObtainByEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'email',
        )
        read_only_fields = ['email', ]

    def validate(self, data):
        user = get_object_or_404(User, email=data.get('email'))
        return data

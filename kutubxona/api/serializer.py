from rest_framework import serializers
from main.models import BookData
from django.contrib.auth import get_user_model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookData
        fields = ('name', 'writer', 'description', 'cost',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)

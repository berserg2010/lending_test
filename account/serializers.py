from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Customer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Customer.objects.create(user=user)
        return user


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            'user',
            'phone',
        )

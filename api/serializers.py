from rest_framework import serializers
from restaurants.models import Restaurant
from app_name.models import ModelName
from .serializers import CreateSerializer

class CreateView(CreateAPIView):
    serializer_class = CreateSerializer


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
            ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]
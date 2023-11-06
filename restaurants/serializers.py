# restaurants/serializers.py

from rest_framework import serializers
from first_app.models import Restaurant, Rating_Mod,UserProfile

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating_Mod
        fields = '__all__'

class Favoriteserial(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields='__all__'

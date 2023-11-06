from rest_framework import serializers
from first_app.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class Dishserializer(serializers.ModelSerializer):
    class Meta:
        model=Dish
        fields= '__all__'

class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields= '__all__'

class Orderitemserializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields= '__all__'
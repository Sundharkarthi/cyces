
from django.http.response import Http404
from first_app.models import Restaurant
from rest_framework.views import APIView
from filtering.serializers import RestaurantSerializer
from rest_framework.response import Response

# Create your views here.
class FilteredRestaurants(APIView):
    def get(self, request, selected_address):
        # Filter restaurants by the selected address
        queryset = Restaurant.objects.filter(address=selected_address)
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
class AddressList(APIView):
    def get(self, request):
        # Retrieve a list of distinct addresses
        addresses = Restaurant.objects.values_list('address', flat=True).distinct()
        address_list = list(addresses)
        return Response(address_list, status=200)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Restaurant
# from .serializers import RestaurantSerializer

class FilteredRestaurantsByRating(APIView):
    def get(self, request, selected_rating):
        # Filter restaurants by the selected rating
        queryset = Restaurant.objects.filter(rating=selected_rating)
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data, status=200)



# from django.contrib.auth.models import User
from rest_framework import permissions,viewsets
from first_app.models import *
from filtering.serializers import *

class Dishview(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = Dishserializer


class Ordersview(APIView):
    def get(self, request):
        restaurants = Orders.objects.all()
        serializer = Orderserializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        serializer=Orderserializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={
            'message':'created',
            'data':serializer.data
        }
        return response

class Ordersitemview(APIView):
    def get(self, request):
        restaurants = OrderItem.objects.all()
        serializer = Orderitemserializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        serializer=Orderitemserializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={
            'message':'created',
            'data':serializer.data
        }
        return response
 # permission_classes = [permissions.IsAuthenticated]

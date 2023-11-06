from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from first_app.models import Restaurant, UserProfile, Rating_Mod
from restaurants.serializers import RestaurantSerializer, RatingSerializer,Favoriteserial

class RestaurantListView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response({'restaurants': serializer.data})

    def post(self,request):
        data=request.data
        serializer=RestaurantSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={
            'message':'created',
            'data':serializer.data
        }
        return response

class AddFavoriteView(APIView):
    @login_required

    def get(self,request):
        user=UserProfile.objects.all()
        serializer=Favoriteserial(user)
        return Response({'favorite': serializer.data})

    def post(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.favorites.add(restaurant)
        return Response({'message': 'Restaurant added to favorites successfully.'})

class RateRestaurantView(APIView):
    @login_required
    def post(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant=restaurant, user=request.user)
            return Response({'message': 'Rating and review submitted successfully.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditRatingView(APIView):
    @login_required
    def get(self, request, rating_id):
        rating = get_object_or_404(Rating_Mod, pk=rating_id)
        if rating.user == request.user:
            serializer = RatingSerializer(rating)
            return Response(serializer.data)
        return Response({'message': 'You do not have permission to edit this rating.'})

    @login_required
    def put(self, request, rating_id):
        rating = get_object_or_404(Rating_Mod, pk=rating_id)
        if rating.user == request.user:
            serializer = RatingSerializer(rating, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Rating and review updated successfully.'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'You do not have permission to edit this rating.'})

class DeleteRatingView(APIView):
    @login_required
    def delete(self, request, rating_id):
        rating = get_object_or_404(Rating_Mod, pk=rating_id)
        if rating.user == request.user:
            rating.delete()
            return Response({'message': 'Rating and review deleted successfully.'})
        return Response({'message': 'You do not have permission to delete this rating.'})




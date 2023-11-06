
from django.http.response import Http404
from first_app.models import Restaurant
from rest_framework.views import APIView
from filtering.serializers import RestaurantSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
import json
from django.shortcuts import render, redirect
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



class Order(APIView):

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        # count=request.POST.get('count')

        # Initialize the count to 0
        count = 0

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = Dish.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []
        #
        # for item in order_items['items']:
        #     price += item['price']
        #     item_ids.append(item['id'])
        #     count += 1

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            # count=count
        )
        order.items.add(*item_ids)

        # After everything is done, send confirmation email to the user
        body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
                f'Your total: {price}\n'
                'Thank you again for your order!')

        send_mail(
            'Thank You For Your Order!',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )

        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('order-confirmation', pk=order.pk)



class OrderConfirmation(APIView):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')
class OrderPayConfirmation(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/order_pay_confirmation.html')


from rest_framework.views import APIView
import random  # generate a random number
from rest_framework.response import Response
from .email import *
from first_app.models import *


class fpassword(APIView):
    def post(self, request):
        print("creating obj")
        email_id = request.data['email']

        try:
            use = User.objects.get(email=email_id)

        except:
                return Response({"message": "email not found"}, status=403)
        n = random.randrange(100000, 999999)  # generating a random number
        otp = n
        print(otp, "otp")
        message = f"""Greetings  from Cyces Restaurant
                    OTP for changing your password is
                    {otp}

                    Have a Good day



                    Thankyou
                    Cyces
                    """
        print("31")

        email_trigger.sendemail(email_id, message)
        print("33")
        for_pass = f_pass.objects.create(email=email_id, otp=otp)
        return Response({"message": "email sent successfull......"})


class verify(APIView):
    def post(self, request):
        try:
            getobj = f_pass.objects.filter(email=request.data['email']).last()
            if getobj.otp == request.data['otp']:
                getobj.delete()
                return Response({"message": "otp verified"})
            else:
                return Response({"message": "wrong otp"}, status=403)

        except:
            return Response({"message": "otp not exist"}, status=403)


class reset(APIView):
    def post(self, request):

        try:
            use = User.objects.get(email=request.data['email'])

        except:
                return Response({"message": "email not found"}, status=403)

        use.set_password(request.data['password'])
        use.save()
        return Response({'message': 'Password reset success'})


import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status


class login_view(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')  # .decode('utf-8')

        return Response({

            'jwt': token,
            'id': user.id,

        })


import openai  # Import the OpenAI module

# Set your OpenAI API key
openai.api_key = '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'
#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

#'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'
#cf4ccb5d-e263-440e-a8b5-b30a4f82c5ee
class DishDescriptionView(APIView):
    def post(self, request):
        dish_name = request.data.get('dish_name')  # Assuming 'dish_name' is sent in the request

        if not dish_name:
            return Response({'error': 'Dish name is required.'}, status=400)

        # Call the OpenAI API to generate a description for the dish
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Describe the dish: {dish_name}",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )

        # Extract the generated description
        description = response.choices[0].text

        # Create a Django Response with the description
        return Response({'description': description}, status=200)


class Calorie_count(APIView):
    def post(self, request):
        dish_name = request.data.get('dish_name')  # Assuming 'dish_name' is sent in the request

        if not dish_name:
            return Response({'error': 'Dish name is required.'}, status=400)

        # Call the OpenAI API to generate a description for the dish
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"calculate the calory count for the {dish_name}, and return the calory count ",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )

        # Extract the generated description
        description = response.choices[0].text

        # Create a Django Response with the description
        return Response({'description': description}, status=200)









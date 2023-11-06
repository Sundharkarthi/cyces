from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from first_app.models import Dish, Orders,OrderItem
from rest_framework import status
from django.shortcuts import get_object_or_404
# @csrf_exempt
# @permission_classes([IsAuthenticated])
class CreateOrder(APIView):
    def post(self, request):

        # import pdb
        # pdb.set_trace()
        response_data = {'success': False, 'message': ''}
        dish_id = request.data.get('dish')
        quantity = request.data.get('order_count')
        if not dish_id or not quantity:
            response_data['message'] = 'Dish and order count are required in the request.'
            return JsonResponse(response_data, status=404)
        try:
            dish = Dish.objects.get(id=dish_id)
            quantity = int(quantity)
            cost = dish.price * quantity

            user_order, created = Orders.objects.get_or_create(user=request.data.get('user'))

            # Create or update the order item
            order_item, created = OrderItem.objects.get_or_create(dish=dish, order=user_order, order_count=quantity,
                                                                  total_price=cost)

            # Calculate the total cost for the order
            total_cost = sum(item.total_price for item in user_order.orderitem_set.all())
            response_data['total_cost'] = cost

            response_data['success'] = True
            response_data['message'] = 'Order item added successfully.'

        except Dish.DoesNotExist:
            response_data['message'] = 'Dish not found.'
        except Exception as e:
            response_data['message'] = 'An error occurred.'
        return JsonResponse(response_data)
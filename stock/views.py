# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# from rest_framework.response import Response
# from first_app.models import Dish,OrderItem
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def place_order(request):
#     # Get the product based on the provided product_id
#     import pdb
#     pdb.set_trace()
#     if request.method == 'POST':
#         new=request.data.get('dish_id')
#         new2=request.data.get('order_count')
#         print(new)
#         print(new2)
#         product = get_object_or_404(Dish, id=new)
#         order_count=get_object_or_404(OrderItem,id=new2)
#         # Check if there is enough stock to fulfill the order
#         if product.count >= order_count.order_count:
#             # Subtract the order count from the stock
#             product.count -= order_count
#             product.save()
#             response_data = {'message': f'Order placed for {order_count} units of {product.dishes}'}
#             print(response_data)
#             # return Response(response_data)
#         else:
#             response_data = {'message': 'Out of Stock'}
#         return JsonResponse(response_data)
#     else:
#         pass
#

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from first_app.models import Dish, OrderItem
from django.shortcuts import get_object_or_404

class PlaceOrder(APIView):
    def post(self, request):
        # Get the data from the request
        # import pdb
        # pdb.set_trace()
        dish_id = request.data.get('dish_id')
        order_count_id = request.data.get('order_count')
        try:
            # Get the product (Dish) and order count (OrderItem) based on the provided dish_id and order_count
            product = get_object_or_404(Dish, id=dish_id)
            order_count = get_object_or_404(OrderItem, id=order_count_id)
            # Check if there is enough stock to fulfill the order
            if product.count >= order_count.order_count:
                # Subtract the order count from the stock
                product.count -= order_count.order_count
                product.save()
                response_data = {'message': f'Order placed for {order_count.order_count} units of {product.dishes}'}
            else:
                response_data = {'message': 'Out of Stock'}

            return Response(response_data, status=status.HTTP_200_OK)

        except Dish.DoesNotExist:
            response_data = {'message': 'Dish not found'}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except OrderItem.DoesNotExist:
            response_data = {'message': 'Order item not found'}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {'message': 'An error occurred'}
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from first_app import views
from rest_framework import routers
from snippets.views import *
from filtering.views import *
from stock.views import PlaceOrder
from stock_count.views import CreateOrder
router=routers.DefaultRouter()
router.register(r'users',views.Userview)

from filtering.views import FilteredRestaurants,AddressList,FilteredRestaurantsByRating
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('accounts/',include('allauth.urls')),
    path('create/',SnippetList.as_view()),
    path('random/',random_number.as_view()),
    path('',include('login.urls')),
    path('',include('restaurants.urls')),
    path('filter/<str:selected_address>/',FilteredRestaurants.as_view()),
    path('list/',AddressList.as_view()),
    path('filter_rating/<int:selected_rating>/',FilteredRestaurantsByRating.as_view()),
    path('dishes/',Dishview.as_view({'get':'list'})),
    path('orders/',Ordersview.as_view()),
    path('stock_count/',PlaceOrder.as_view()),
    path('create_order/',CreateOrder.as_view()),
    path('ordersitem/',Ordersitemview.as_view())
    # path('des/<int:pk>',SnippetDetail.as_view()),
    # path('',include('snippets.urls')),
]

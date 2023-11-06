from rest_framework.routers import DefaultRouter
# from restaurants.views import RestaurantViewSet
from django.urls import path,include
from login.views import LoginView
from restaurants.views import RestaurantListView, AddFavoriteView, RateRestaurantView, EditRatingView, DeleteRatingView



urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('favorites/<int:restaurant_id>/', AddFavoriteView.as_view(), name='add_favorite'),
    path('rate/<int:restaurant_id>/', RateRestaurantView.as_view(), name='rate_restaurant'),
    path('edit/<int:rating_id>/', EditRatingView.as_view(), name='edit_rating'),
    path('delete/<int:rating_id>/', DeleteRatingView.as_view(), name='delete_rating'),
    # path('api/', include(router.urls)),

    # path('admin/', admin.site.urls),
    # path('login_old/',LoginView.as_view()),
    # path('', include('login_new.urls')),

]

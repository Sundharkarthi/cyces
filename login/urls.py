# authentication/urls.py

from django.urls import path
from login import views
from django.urls import path
from login.views import CustomLoginView, CustomLogoutView, CustomPasswordResetView, CustomPasswordResetDoneView
from login.views import CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomPasswordChangeView
from login.views import CustomPasswordChangeDoneView, CustomRegisterView,CustomLoginView_new

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('adminlogin/', CustomLoginView_new.as_view(), name='adminlogin'),
]
#
# urlpatterns = [
#     path('login/', views.CustomLoginView.as_view(), name='login'),
#     path('register/', views.RegisterView.as_view(), name='register'),
# ]

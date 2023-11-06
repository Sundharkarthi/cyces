from django.contrib import admin
from django.contrib.auth.models import User
from first_app.models import Snippet
from first_app.models import Restaurant,UserProfile,User,Dish,Orders,OrderItem

admin.site.register(Snippet)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Orders)
admin.site.register(OrderItem)
# admin.site.register(User)
# Register your models here.

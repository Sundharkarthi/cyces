

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.db import models
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

from django.contrib.auth.base_user import AbstractBaseUser
# from django.db import models
# from django.contrib.auth.models import User


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    password = models.CharField(max_length=255, blank=False)
    # alternate_phonenumber = models.CharField(max_length=15, blank=True)
    addressline_one = models.CharField(max_length=100, blank=False)
    # addressline_two = models.CharField(max_length=100, blank=True)
    countryor_city = models.CharField(max_length=100, blank=False)
    postalcode = models.CharField(max_length=100, blank=False)
    company_name = models.CharField(max_length=100, blank=True)
    # company_type = models.CharField(max_length=100, blank=True)
    # category = models.CharField(max_length=100, blank=False)
    role=models.CharField(max_length=100)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "register"




class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
        # db_table="Snippet"

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Restaurant, blank=True)

    def __str__(self):
        return self.user


class Rating_Mod(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    review = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant
class Dish(models.Model):
    restaurant= models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dishes=models.CharField(max_length=100)
    count=models.IntegerField()
    price=models.IntegerField(default=100)

    def __str__(self):
        return f"{self.dishes}{self.count}{self.restaurant}{self.price}"

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dishes=models.ManyToManyField(Dish,blank=True,through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    # order_count=models.IntegerField()
    # total_price=models.IntegerField()

class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    order_count = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)




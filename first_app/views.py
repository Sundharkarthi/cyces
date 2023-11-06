from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions,viewsets
from first_app.serializers import Userserializer

class Userview(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.

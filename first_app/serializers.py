from django.contrib.auth.models import User,Group
from rest_framework import serializers


class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url', 'username', 'email']
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User,Group
from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserExtensionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserExtensionModel
        fields = ('user','sex','age','photo')
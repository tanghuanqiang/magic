from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
class PersonSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = Person
        fields = "__all__"
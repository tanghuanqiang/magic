from django_filters import rest_framework as filter
from .models import *

class PersonFilter(filter.FilterSet):
    class Meta:
        model = Person
        fields = {'name':['exact'],}   
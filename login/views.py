from django.shortcuts import render
from rest_framework import status,viewsets,permissions
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from .models import *
from .serializers import *
from .filter import *
ALLOW_METHODS = ('GET', 'HEAD', 'POST','OPTIONS')
class IsOwnerOrPostOnly(permissions.BasePermission):
    """
        允许没有权限的用户查看和提交表单
        有权限的用户可以任意操作
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ALLOW_METHODS:
            return True
        
        return obj.owner == request.user
# Create your views here.
class PersonlistViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,BasicAuthentication,)
    permission_classes = IsOwnerOrPostOnly
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_class = PersonFilter
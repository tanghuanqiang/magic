from django.shortcuts import render
from rest_framework import status,viewsets,permissions
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from .models import *
from .serializers import *
from .filter import *
class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的 API 端点。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的 API 端点。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class UserExtensionViewSet(viewsets.ModelViewSet):
    queryset = UserExtensionModel.objects.all()
    serializer_class = UserExtensionSerializer
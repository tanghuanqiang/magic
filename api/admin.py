from django.contrib import admin
from .models import *
# Register your models here.
# class UserExtensionAdmin(admin.ModelAdmin):
#     fields=['user','sex','age','photo']
admin.site.register(UserExtensionModel)
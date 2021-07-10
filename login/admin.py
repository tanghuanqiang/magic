from django.contrib import admin
from .models import *
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    fields = ['name','sex','photo']

admin.site.register(Person,PersonAdmin)
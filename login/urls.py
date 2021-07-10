from django.conf.urls import url
from .views import *
from rest_framework import routers,renderers,urlpatterns

router = routers.DefaultRouter()
router.register(r'login', PersonlistViewset)

urlpatterns = router.urls
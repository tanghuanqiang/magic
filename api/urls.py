from django.conf.urls import include
from .views import *
from rest_framework import routers,renderers,urlpatterns

router = routers.DefaultRouter()
router.register(r'userextensionmodel', UserExtensionViewSet)


urlpatterns = router.urls
from django.urls import path,include
from .views import LocationViewset,HelperServiceViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('location',LocationViewset)
router.register('helperservice',HelperServiceViewset)


urlpatterns = [
    path('',include(router.urls)),
]

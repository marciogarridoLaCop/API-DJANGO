from django.contrib import admin
from django.urls import path,include
from DataLogSensor.views import RegistroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('DataLogSensor', RegistroViewSet, basename='Registro')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) )
]
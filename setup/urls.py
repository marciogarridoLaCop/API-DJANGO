from django.contrib import admin
from django.urls import path,include
from DataLogSensor.views import RegistroViewSet
from Device.views import TipoViewSet,SensorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Tipo', TipoViewSet, basename='Tipo')
router.register('Sensor', SensorViewSet, basename='Sensor')
router.register('DataLogSensor', RegistroViewSet, basename='Registro')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    
]
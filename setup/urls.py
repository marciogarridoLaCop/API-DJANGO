from django.contrib import admin
from django.urls import path,include
from DataLog.views import RegistroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('DataLog', RegistroViewSet, basename='Registro')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) )
]
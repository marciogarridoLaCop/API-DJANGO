from rest_framework import viewsets, filters
from DataLogSensor.models import Registro
from DataLog.serializer import RegistroSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class RegistroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os registros"""
    queryset = Registro.objects.all()
    serializer_class =  RegistroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['sensor']
    search_fields = ['sensor__sensor']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
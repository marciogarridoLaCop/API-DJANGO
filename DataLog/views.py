from rest_framework import viewsets, filters
from DataLog.models import Registro
from DataLog.serializer import RegistroSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RegistroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os registros"""
    queryset = Registro.objects.all()
    serializer_class =  RegistroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['sensor']
    search_fields = ['sensor__sensor']


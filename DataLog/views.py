from rest_framework import viewsets
from DataLog.models import Registro
from DataLog.serializer import RegistroSerializer


class RegistroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os registros"""
    queryset = Registro.objects.all()
    serializer_class =  RegistroSerializer

from rest_framework import viewsets,generics
from DataLogSensor.models import Registro
from DataLogSensor.serializer import RegistroSerializer,ListaRegistroSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class RegistroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os registros"""
    queryset = Registro.objects.all()
    serializer_class =  RegistroSerializer
    paginate_by = None
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaRegistroSensor(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Registro.objects.filter(sensor_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaRegistroSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
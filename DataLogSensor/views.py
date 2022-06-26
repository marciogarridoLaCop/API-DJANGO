from rest_framework import viewsets,generics
from DataLogSensor.models import Registro
from Device.models import Tipo,Sensor
from DataLogSensor.serializer import RegistroSerializer, VisualizarRegistroSerializer
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


class ListaRegistro(generics.ListAPIView):
    """Listando os sensores"""
    def get_queryset(self):
        queryset = Registro.objects.filter(sensor_id=self.kwargs['pk'])
        return queryset
    serializer_class = VisualizarRegistroSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    
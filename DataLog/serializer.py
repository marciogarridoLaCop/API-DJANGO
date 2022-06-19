from rest_framework import serializers
from DataLog.models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['id', 'sensor', 'temperatura', 'umidade', 'pressao']

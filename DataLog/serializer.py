from rest_framework import serializers
from DataLog.models import Registro
from DataLog.validators import *

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['id', 'sensor', 'temperatura', 'umidade', 'pressao']
        
    def validate(self, data):
        if temperarura_valida(data['temperatura']):
            raise serializers.ValidationError({'temperatura':"A temperatura precisa ter um valor numérico"})
        if not temperarura_tamanho(data['temperatura']):
            raise serializers.ValidationError({'temperatura':"A temperatura precisa ter um valor no máximo 5 dígitos"})   
        if umidade_valida(data['umidade']):
            raise serializers.ValidationError({'umidade':"A umidade precisa ter um valor numérico"})
        if pressao_valida(data['pressao']):
            raise serializers.ValidationError({'pressao':"A pressão precisa ter um valor numérico"})
        return data

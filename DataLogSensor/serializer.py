from rest_framework import serializers
from DataLogSensor.models import Registro
from DataLogSensor.validators import *

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['id', 'sensor', 'temperatura', 'pressao','altitude','pressa_nivel_mar','altitude_real']
        
    def validate(self, data):
        if temperarura_valida(data['temperatura']):
            raise serializers.ValidationError({'temperatura':"A temperatura precisa ter um valor numérico"})
        if not temperarura_tamanho(data['temperatura']):
            raise serializers.ValidationError({'temperatura':"A temperatura precisa ter um valor no máximo 5 dígitos"})   
        if pressao_valida(data['pressao']):
            raise serializers.ValidationError({'pressao':"A pressão precisa ter um valor numérico"})
        if altitude_valida(data['altitude']):
            raise serializers.ValidationError({'altitude':"A altiude precisa ter um valor numérico"})
        if pressao_nivel_valida(data['pressa_nivel_mar']):
            raise serializers.ValidationError({'pressa_nivel_mar':"A Pressão a nível do mar precisa ter um valor numérico"})
        if altidude_real_valida(data['altitude_real']):
            raise serializers.ValidationError({'altitude_real':"A Altidude real precisa ter um valor numérico"})
        
        return data

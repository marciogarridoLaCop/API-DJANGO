from django.db import models
from Device.models import Tipo,Sensor
from datetime import datetime

class Registro(models.Model):

    format_data = '%d/%m/%y %H:%M'
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime(format_data)
    
    sensor = models.ForeignKey(Sensor, blank=False, null=False,on_delete=models.CASCADE,verbose_name = 'Identificação do Sensor')
    temperatura = models.CharField(max_length=9,blank=False, null=False,verbose_name = 'Temperatura')
    umidade = models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Umidade')
    pressao = models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Pressão')
    data_registro = data_e_hora_em_texto

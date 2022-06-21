from wsgiref.handlers import format_date_time
from django.db import models
from Device.models import Tipo,Sensor
from datetime import datetime

class Registro(models.Model):

    # inicialização das variaveis e seus parametros
    sensor = models.ForeignKey(Sensor, blank=False, null=False,on_delete=models.CASCADE,verbose_name = 'Identificação do Sensor')
    temperatura = models.CharField(max_length=9,blank=False, null=False,verbose_name = 'Temperatura')
    umidade = models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Umidade')
    pressao = models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Pressão')
    data_registro = models.DateTimeField(auto_now=True,verbose_name='Data do registro') 
  
    def __str__(self):
        return self.sensor
from django.db import models

class Tipo(models.Model):
    nome = models.CharField(max_length=30,blank=False, null=False, verbose_name='Tipo do sensor')

    def __str__(self):
        return self.nome

class Sensor(models.Model):
    sensor = models.CharField(max_length=30,blank=False,verbose_name = 'Nome do sensor')
    tipo = models.ForeignKey(Tipo,blank=False, on_delete=models.CASCADE)
    local = models.CharField(max_length=11 ,blank=False, null= False, verbose_name = 'Local de Instalação')
    macaddress = models.CharField(max_length=11 ,null=False,verbose_name = 'Endereço MAC')
    data_cadastro = models.DateField()

    def __str__(self):
        return self.sensor

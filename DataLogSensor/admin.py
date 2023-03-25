from django.contrib import admin
from DataLogSensor.models import Registro

class Dados(admin.ModelAdmin):
    list_display = ('id','sensor','temperatura','pressao','precipitacao','altitude','pressa_nivel_mar','altitude_real','data_registro')
    list_display_links = ('id', 'sensor')
    search_fields = ('sensor',)
    list_per_page = 10000
    ordering =('data_registro',)

admin.site.register(Registro,Dados)

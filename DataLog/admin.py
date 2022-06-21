from django.contrib import admin

from DataLog.models import Registro

class Dados(admin.ModelAdmin):
    list_display = ('id','sensor','temperatura','umidade','pressao','data_registro')
    list_display_links = ('id', 'sensor')
    search_fields = ('sensor',)
    list_per_page = 20
    ordering =('data_registro',)

admin.site.register(Registro,Dados)
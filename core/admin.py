from django.contrib import admin
from .models import *
# Register your models here.


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nome_empresa', 'categoria_empresa', 'quitado')

class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'valor')

admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Stand, StandAdmin)
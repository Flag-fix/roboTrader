from django.contrib import admin
from .models import Cidade,Equipamento,Tipo,Pessoa,OrdemServico

admin.site.register(Cidade)
admin.site.register(Equipamento)
admin.site.register(Tipo)
admin.site.register(Pessoa)
admin.site.register(OrdemServico)

# Register your models here.

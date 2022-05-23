from django.contrib import admin
from .models import Cidade,Equipamento,TipoEquipamento,Pessoa,OrdemServico

admin.site.register(Cidade)
admin.site.register(Equipamento)
admin.site.register(TipoEquipamento)
admin.site.register(Pessoa)
admin.site.register(OrdemServico)

# Register your models here.

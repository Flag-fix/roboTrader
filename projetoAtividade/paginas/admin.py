from django.contrib import admin
from .models import Cidade,Atividade,Demanda,Pessoa,Setor

admin.site.register(Cidade)
admin.site.register(Atividade)
admin.site.register(Demanda)
admin.site.register(Pessoa)
admin.site.register(Setor)

# Register your models here.

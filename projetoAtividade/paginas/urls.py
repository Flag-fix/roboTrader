from django.urls import path
from .views import index, CidadeCreate,SetorCreate,PessoaCreate,DemandaCreate,AtividadeCreate
from .views import SetorUpdate,CidadeUpdate,PessoaUpdate,DemandaUpdate,AtividadeUpdate


urlpatterns = [

    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastrar/setor/', SetorCreate.as_view(), name='cadastrar-setor'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('cadastrar/demanda/', DemandaCreate.as_view(), name='cadastrar-demanda'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),

    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('editar/setor/<int:pk>/', SetorUpdate.as_view(), name='editar-setor'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('editar/demanda/<int:pk>/', DemandaUpdate.as_view(), name='editar-demanda'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),


    path('', index.as_view(), name='Index'),
]
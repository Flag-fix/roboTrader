from django.urls import path
from .views import index, SetorCreate, CidadeCreate, PessoaCreate, DemandaCreate, AtividadeCreate
from .views import SetorUpdate,CidadeUpdate,PessoaUpdate,DemandaUpdate,AtividadeUpdate
from .views import SetorDelete,CidadeDelete,PessoaDelete, DemandaDelete, AtividadeDelete
from .views import SetorList,CidadeList,PessoaList, DemandaList,AtividadeList

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

    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('excluir/setor/<int:pk>/', SetorDelete.as_view(), name='excluir-setor'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    path('excluir/demanda/<int:pk>/',
         DemandaDelete.as_view(), name='excluir-demanda'),
    path('excluir/atividade/<int:pk>/',
         AtividadeDelete.as_view(), name='excluir-atividade'),


    path('listar/cidade/', CidadeList.as_view(), name='listar-cidade'),
    path('listar/setor/', SetorList.as_view(), name='listar-setor'),
    path('listar/pessoa/', PessoaList.as_view(), name='listar-pessoa'),
    path('listar/demanda/', DemandaList.as_view(), name='listar-demanda'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade'),



    path('', index.as_view(), name='index'),
]
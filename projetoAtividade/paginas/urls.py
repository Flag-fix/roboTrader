from django.urls import path
from .views import index, OrdemServicoCreate, CidadeCreate, PessoaCreate, TipoCreate, EquipamentoCreate
from .views import OrdemServicoUpdate, CidadeUpdate, PessoaUpdate, TipoUpdate, EquipamentoUpdate
from .views import OrdemServicoDelete, CidadeDelete, PessoaDelete, TipoDelete, EquipamentoDelete
from .views import OrdemServicoList, CidadeList, PessoaList, TipoList, EquipamentoList, OrdemServicoUsuarioList

urlpatterns = [

    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastrar/ordemServico/', OrdemServicoCreate.as_view(), name='cadastrar-ordemServico'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('cadastrar/tipo/', TipoCreate.as_view(), name='cadastrar-tipo'),
    path('cadastrar/equipamento/', EquipamentoCreate.as_view(), name='cadastrar-equipamento'),

    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('editar/ordemServico/<int:pk>/', OrdemServicoUpdate.as_view(), name='editar-ordemServico'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name='editar-tipo'),
    path('editar/equipamento/<int:pk>/', EquipamentoUpdate.as_view(), name='editar-equipamento'),

    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('excluir/ordemServico/<int:pk>/', OrdemServicoDelete.as_view(), name='excluir-ordemServico'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    path('excluir/tipo/<int:pk>/',
         TipoDelete.as_view(), name='excluir-tipo'),
    path('excluir/equipamento/<int:pk>/',
         EquipamentoDelete.as_view(), name='excluir-equipamento'),

    path('listar/cidade/', CidadeList.as_view(), name='listar-cidade'),
    path('listar/ordemServico/', OrdemServicoList.as_view(), name='listar-ordemServico'),
    path('listar/minhas-ordem-servico/', OrdemServicoUsuarioList.as_view(), name='listar-ordemServico-usuario'),
    path('listar/pessoa/', PessoaList.as_view(), name='listar-pessoa'),
    path('listar/tipo/', TipoList.as_view(), name='listar-tipo'),
    path('listar/equipamento/', EquipamentoList.as_view(), name='listar-equipamento'),

    path('', index.as_view(), name='index'),
]

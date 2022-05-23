from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Cidade, Pessoa, OrdemServico, Equipamento, TipoEquipamento

class index(TemplateView):
    template_name = 'paginas/index.html'

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['descricao', 'nascimento', 'email', 'senha', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['descricao', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class SetorCreate(CreateView):
    model = OrdemServico
    fields = ['descricao',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class AtividadeCreate(CreateView):
    model = Equipamento
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class DemandaCreate(CreateView):
    model = TipoEquipamento
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['descricao', 'nascimento', 'email', 'senha', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['descricao', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class SetorUpdate(UpdateView):
    model = OrdemServico
    fields = ['descricao',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class AtividadeUpdate(UpdateView):
    model = Equipamento
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class DemandaUpdate(UpdateView):
    model = TipoEquipamento
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

#=##############
class DemandaDelete(DeleteView):
    model = TipoEquipamento
    template_name = 'cadastros/form-delete.html'
    sucess_url = reverse_lazy('index')
    

class AtividadeDelete(DeleteView):
    model = Equipamento
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class SetorDelete(DeleteView):
    model = OrdemServico
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-pessoa')


class PessoaList(ListView):
    model = Pessoa
    template_name = 'paginas/listas/pessoa.html'
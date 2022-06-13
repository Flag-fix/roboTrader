from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin


from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cidade, Pessoa, Setor, Atividade, Demanda

class index(TemplateView):
    template_name = 'paginas/index.html'

class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class SetorCreate(LoginRequiredMixin, CreateView):
    model = Setor
    fields = ['nome',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class AtividadeCreate(LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class DemandaCreate(LoginRequiredMixin, CreateView):
    model = Demanda
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(LoginRequiredMixin, GroupRequiredMixin,  UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento','cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')
    group_required = u"Administrador"

class CidadeUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    group_required = u"Administrador"

class SetorUpdate(LoginRequiredMixin, GroupRequiredMixin,  UpdateView):
    model = Setor
    fields = ['nome',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    group_required = u"Administrador"

class AtividadeUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Atividade
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    group_required = u"Administrador"

class DemandaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Demanda
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    group_required = u"Administrador"
#=##############


class DemandaDelete(LoginRequiredMixin, GroupRequiredMixin,  DeleteView):
    model = Demanda
    template_name = 'cadastros/form-delete.html'
    sucess_url = reverse_lazy('index')
    group_required = u"Administrador"

class AtividadeDelete(LoginRequiredMixin, GroupRequiredMixin,  DeleteView):
    model = Atividade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')
    group_required = u"Administrador"

class SetorDelete(LoginRequiredMixin, GroupRequiredMixin,  DeleteView):
    model = Setor
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')
    group_required = u"Administrador"

class CidadeDelete(LoginRequiredMixin, GroupRequiredMixin,  DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')
    group_required = u"Administrador"

class PessoaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-pessoa')
    group_required = u"Administrador"

class PessoaList(LoginRequiredMixin, GroupRequiredMixin,  ListView):
    model = Pessoa
    template_name = 'paginas/listas/pessoa.html'
    group_required = u"Administrador"

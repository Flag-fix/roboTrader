from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Cidade, Pessoa, Setor, Atividade, Demanda

class index(TemplateView):
    template_name = 'paginas/index.html'

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'senha', 'cidade']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class SetorCreate(CreateView):
    model = Setor
    fields = ['nome',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class DemandaCreate(CreateView):
    model = Demanda
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'senha', 'cidade']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class SetorUpdate(UpdateView):
    model = Setor
    fields = ['nome',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')


class DemandaUpdate(UpdateView):
    model = Demanda
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    succes_url = reverse_lazy('index')

from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Cidade, Pessoa, OrdemServico, Equipamento, Tipo


class index(TemplateView):
    template_name = 'paginas/index.html'


class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'tipo_pessoa', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')

    # def form_valid(self, form):
    #     # form.instance.nome_do_atributo = valor
    #     form.instance.usuario = self.request.user
    #
    #     # só tem no create view
    #
    #     # validando os dados do form antes de criar o objeto(nao está no banco)
    #     url = super().form_valid(form)
    #
    #     # aqui vc tem o objeto (dados inseridos no banco)
    #     return url


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')



class OrdemServicoCreate(LoginRequiredMixin, CreateView):
    model = OrdemServico
    fields = ['descricao', 'data_inicial', 'equipamento', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-ordemServico')

    def form_valid(self, form):
        # form.instance.nome_do_atributo = valor
        form.instance.usuario = self.request.user

        # só tem no create view

        # validando os dados do form antes de criar o objeto(nao está no banco)
        url = super().form_valid(form)

        # aqui vc tem o objeto (dados inseridos no banco)
        return url


class EquipamentoCreate(LoginRequiredMixin, CreateView):
    model = Equipamento
    fields = ['nome_equipamento', 'data_entrada', 'status', 'descricao', 'tipo_equipamento']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-equipamento')



class TipoCreate(LoginRequiredMixin, CreateView):
    model = Tipo
    fields = ['nome']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-tipo')



class PessoaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'tipo_pessoa', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')
    group_required = u"Administrador"


class CidadeUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')
    group_required = u"Administrador"


class OrdemServicoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = OrdemServico
    fields = ['descricao', 'data_inicial', 'data_final', 'equipamento', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-ordemServico')
    group_required = u"Administrador"


class OrdemServicoUsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = OrdemServico
    fields = ['descricao', 'data_inicial', 'data_final', 'equipamento', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-ordemServico')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            OrdemServico, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class EquipamentoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Equipamento
    fields = ['nome_equipamento',
              'data_entrada',
              'status',
              'descricao',
              'tipo_equipamento']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-equipamento')
    group_required = u"Administrador"



class TipoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Tipo
    fields = ['nome']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-tipo')
    group_required = u"Administrador"




# =##############
class TipoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Tipo
    template_name = 'paginas/form-delete.html'
    sucess_url = reverse_lazy('listar-tipo')
    group_required = u"Administrador"




class EquipamentoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Equipamento
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-equipamento')
    group_required = u"Administrador"



class OrdemServicoUsusarioDelete(LoginRequiredMixin, DeleteView):
    model = OrdemServico
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-ordemServico')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            OrdemServico, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class OrdemServicoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = OrdemServico
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-ordemServico')
    group_required = u"Administrador"


class CidadeDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-cidade')
    group_required = u"Administrador"



class PessoaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-pessoa')
    group_required = u"Administrador"


class TipoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Tipo
    template_name = 'paginas/listas/tipo.html'
    group_required = u"Administrador"



class EquipamentoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Equipamento
    template_name = 'paginas/listas/equipamento.html'
    group_required = u"Administrador"



class OrdemServicoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = OrdemServico
    template_name = 'paginas/listas/ordemServico.html'
    group_required = u"Administrador"


class OrdemServicoUsuarioList(LoginRequiredMixin, ListView):
    model = OrdemServico
    template_name = 'paginas/listas/ordemServico.html'

    def get_queryset(self):
        self.object_list = OrdemServico.objects.filter(usuario=self.request.user)
        return self.object_list


class CidadeList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Cidade
    template_name = 'paginas/listas/cidade.html'
    group_required = u"Administrador"


class PessoaList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Pessoa
    template_name = 'paginas/listas/pessoa.html'
    group_required = u"Administrador"


class PaginaInicialView(TemplateView):
    template_name = 'paginas/index.html'

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(self, *args, **kwargs)

        if self.request.user.is_authenticated:
            dados["pessoas"] = Equipamento.objects.filter(
                equipamento__usuario=self.request.user,
                is_urgente__isnull=False
            )

        else:
            dados["pessoas"] = 0
        return dados

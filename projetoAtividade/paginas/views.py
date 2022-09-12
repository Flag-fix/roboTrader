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

    def form_valid(self, form):
        # form.instance.nome_do_atributo = valor
        form.instance.usuario = self.request.user

        # só tem no create view

        # validando os dados do form antes de criar o objeto(nao está no banco)
        url = super().form_valid(form)

        # aqui vc tem o objeto (dados inseridos no banco)
        return url


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')

    def form_valid(self, form):
        # form.instance.nome_do_atributo = valor
        form.instance.usuario = self.request.user

        # só tem no create view

        # validando os dados do form antes de criar o objeto(nao está no banco)
        url = super().form_valid(form)

        # aqui vc tem o objeto (dados inseridos no banco)
        return url


class OrdemServicoCreate(LoginRequiredMixin, CreateView):
    model = OrdemServico
    fields = ['descricao', 'data_inicial', 'data_final', 'equipamento', 'status']
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

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, *kwargs)
        dados["form"].fields["equipamento"].queryset = Equipamento.objects.filter(usuario=self.request.user)

        return dados


class EquipamentoCreate(LoginRequiredMixin, CreateView):
    model = Equipamento
    fields = ['nome_equipamento', 'data_entrada', 'status', 'descricao', 'tipo_equipamento']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-equipamento')

    def form_valid(self, form):
        # form.instance.nome_do_atributo = valor
        form.instance.usuario = self.request.user

        # só tem no create view

        # validando os dados do form antes de criar o objeto(nao está no banco)
        url = super().form_valid(form)

        # aqui vc tem o objeto (dados inseridos no banco)
        return url

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, *kwargs)
        dados["form"].fields["tipo_equipamento"].queryset = Tipo.objects.filter(usuario=self.request.user)

        return dados


class TipoCreate(LoginRequiredMixin, CreateView):
    model = Tipo
    fields = ['nome']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-tipo')

    def form_valid(self, form):
        # form.instance.nome_do_atributo = valor
        form.instance.usuario = self.request.user

        # só tem no create view

        # validando os dados do form antes de criar o objeto(nao está no banco)
        url = super().form_valid(form)

        # aqui vc tem o objeto (dados inseridos no banco)
        # Como por exemplo:
        # self.object.codigo = hash(self.object.pk)
        # aí você tem que salvar o objeto de novo
        # self.object.save()

        return url


class PessoaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'tipo_pessoa', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Pessoa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CidadeUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cidade')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Cidade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class OrdemServicoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = OrdemServico
    fields = ['descricao', 'data_inicial', 'data_final', 'equipamento', 'status']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-ordemServico')
    group_required = u"Administrador"

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

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Equipamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, *kwargs)
        dados["form"].fields["ordemServico"].queryset = OrdemServico.objects.filter(
            usuario=self.request.user)
        return dados


class TipoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Tipo
    fields = ['nome']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-tipo')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Tipo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


# =##############
class TipoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Tipo
    template_name = 'paginas/form-delete.html'
    sucess_url = reverse_lazy('listar-tipo')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Tipo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class EquipamentoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Equipamento
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-equipamento')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Equipamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class OrdemServicoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = OrdemServico
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-ordemServico')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            OrdemServico, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CidadeDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-cidade')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Cidade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class PessoaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-pessoa')
    group_required = u"Administrador"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Pessoa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class TipoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Tipo
    template_name = 'paginas/listas/tipo.html'
    group_required = u"Administrador"

    def get_queryset(self):
        self.object_list = Tipo.objects.filter(usuario=self.request.user)
        return self.object_list


class EquipamentoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Equipamento
    template_name = 'paginas/listas/equipamento.html'
    group_required = u"Administrador"

    def get_queryset(self):
        self.object_list = Equipamento.objects.filter(usuario=self.request.user)
        return self.object_list


class OrdemServicoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = OrdemServico
    template_name = 'paginas/listas/ordemServico.html'
    group_required = u"Administrador"

    def get_queryset(self):
        self.object_list = OrdemServico.objects.filter(usuario=self.request.user)
        return self.object_list


class CidadeList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Cidade
    template_name = 'paginas/listas/cidade.html'
    group_required = u"Administrador"

    def get_queryset(self):
        self.object_list = Cidade.objects.filter(usuario=self.request.user)
        return self.object_list


class PessoaList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Pessoa
    template_name = 'paginas/listas/pessoa.html'
    group_required = u"Administrador"

    def get_queryset(self):
        self.object_list = Pessoa.objects.filter(usuario=self.request.user)
        return self.object_list


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

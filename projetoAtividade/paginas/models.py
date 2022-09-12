from django.db import models
from django.contrib.auth.models import User

# Aqui a gente pode criar varias classes referente a esse assunto.
ESTADOS = [
    ('SP', 'São Paulo'),
    ('PR', 'Paraná'),
    ('SC', 'Santa Catarina')
]

TIPO_PESSOA = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica')
]

STATUS = [('ABERTO', 'ABERTO'), ('FECHADO', 'FECHADO')]


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    estado = models.CharField(max_length=2, choices=ESTADOS)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome + "/" + self.estado


class Pessoa(models.Model):
    # Verbose_name = Mostra o texto na label
    nome_completo = models.CharField(max_length=50, verbose_name="Nome da pessoa",
                                     help_text="Digite seu nome_os completo")
    nascimento = models.DateField(verbose_name='Data de nascimento')
    tipo_pessoa = models.CharField(max_length=2, choices=TIPO_PESSOA)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.nome_completo, self.nascimento)


class Tipo(models.Model):
    nome = models.CharField(
        max_length=100, verbose_name="Tipo", help_text="Hidráulico")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome)


class Equipamento(models.Model):
    nome_equipamento = models.CharField(
        max_length=100, verbose_name="Nome do equipamento", help_text="Digite o nome do equipamento")
    data_entrada = models.DateField(verbose_name='Data da entrada')
    status = models.CharField(max_length=8, choices=STATUS)
    descricao = models.CharField(max_length=100, verbose_name="Descrição do Equipamento")
    tipo_equipamento = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome_equipamento)


class OrdemServico(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    data_inicial = models.DateTimeField(verbose_name='Data Abertura')
    data_final = models.DateTimeField(verbose_name='Data Fechamento', null=True)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    status = models.CharField(max_length=8, choices=STATUS)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.descricao)

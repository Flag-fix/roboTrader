from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + "/" + self.estado
        

class Pessoa(models.Model):
    nome = models.CharField(
        max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    nascimento = models.DateField(
        verbose_name='data de nascimento', blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, unique=True, )
    email = models.EmailField(max_length=255, blank=False, null=False)
    tipo_pessoa = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    senha = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return '{} ({})'.format(self.nome)


class OrdermServico(models.Model):

    descricao = models.TextField(verbose_name="Qual seu problema?", help_text="Informe Descrição da OS")
    data_inicial = models.DateField(
        verbose_name='data inicial', blank=False, null=False)
    data_final = models.DateField(
        verbose_name='data final', blank=False, null=False)
    prioridade = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    senha = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return '{} ({})'.format(self.descricao, self.status)


class TipoEquipamento(models.Model):
    tipo_equipamento = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo_equipamento


class Equipamento(models.Model):
    nome_equipamento = models.CharField(max_length=255)
    descricao = models.TextField(
        verbose_name="Fale sobre o Equipamento")
    tipo_equipamento = models.CharField(
        max_length=255)

    def __str__(self):
        return self.nome_equipamento + "/" + self.tipo_equipamento

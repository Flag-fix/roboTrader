from django.db import models

# Aqui a gente pode criar varias classes referente a esse assunto.
ESTADOS = [('SP', 'São Paulo'), ('PR', 'Paraná')]

TIPO_PESSOA = [('F', 'Física'), ('J', 'Jurídica')]

PRIORIDADE = [('A', 'Alta'), ('M', 'Média'), ('B', 'Baixa'), ('U', 'Urgente')]

STATUS = [('A', 'Aberto'), ('F', 'Fechado')]


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    estado = models.CharField(max_length=2, choices=ESTADOS)

    def __str__(self):
        return self.nome + "/" + self.estado


class Pessoa(models.Model):
    # Verbose_name = Mostra o texto na label
    nome = models.CharField(max_length=50, verbose_name="Nome da pessoa", help_text="Digite seu descricao completo")
    nascimento = models.DateField(verbose_name='Data de nascimento')
    tipo_pessoa = models.CharField(choices=TIPO_PESSOA)
    senha = models.CharField(max_length=100, verbose_name="Senha")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.nascimento)


class OrdemServico(models.Model):
    titulo = models.CharField(verbose_name="Titulo")
    descricao = models.TextField(verbose_name="Descricao")
    data_inicial = models.DateField(verbose_name='Data inicial')
    data_final = models.DateField(verbose_name='Data final')
    prioridade = models.CharField(max_length=2, choices=PRIORIDADE)
    status = models.CharField(max_length=2, choices=STATUS)

    def __str__(self):
        return '{} ({})'.format(self.descricao)


class TipoEquipamento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo ")
    data_inicial = models.DateField(verbose_name='Data de início')
    data_final = models.DateField(verbose_name='Data final')
    og = models.IntegerField(verbose_name="Ordem de grandeza")

    def __str__(self):
        return '{} ({})'.format(self.nome)


class Equipamento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Títulonda", help_text="Digite o título da demanda")
    descricao = models.TextField(verbose_name="Descricao Equipamento")
    data_entrega = models.DateField(verbose_name='Data de entrega')
    tipo_equipamento = models.ForeignKey(TipoEquipamento, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome)

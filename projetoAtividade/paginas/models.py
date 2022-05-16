from django.db import models

# Aqui a gente pode criar varias classes referente a esse assunto.
ESTADOS = [
    ('SP','São Paulo'),
    ('PR','Paraná'),
 ]


class Cidade(models.Model):
    nome = models.CharField(max_length=100,verbose_name="Nome da cidade")
    estado = models.CharField(max_length=2,choices=ESTADOS)
    
    def __str__(self):
        return self.nome + "/" + self.estado


class Pessoa(models.Model):

    #Verbose_name = Mostra o texto na label
    nome_completo = models.CharField(max_length=50, verbose_name="Nome da pessoa", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name='Data de nascimento')
    email = models.CharField(max_length=100,verbose_name="Email")
    senha = models.CharField(max_length=100,verbose_name="Senha")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.nascimento)


class Setor(models.Model):

    nome = models.CharField(max_length=100, verbose_name="Nome do setor")
    area_atuacao = models.CharField(
        max_length=100, verbose_name="Área de atuação")
    email = models.CharField(max_length=100, verbose_name="Email")

    def __str__(self):
        return '{} ({})'.format(self.nome)


class Atividade(models.Model):

    titulo = models.CharField(
        max_length=100, verbose_name="Título da demanda", help_text="Digite o título da demanda")
    data_entrega = models.DateField(verbose_name='Data de entrega')
    status = models.CharField(max_length=100, verbose_name="Status da demanda")
    is_urgente = models.BooleanField(verbose_name="É urgente?")
    descricao = models.CharField(
        max_length=100, verbose_name="Descrição da demanda")
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome)




class Demanda(models.Model):

    titulo = models.CharField(
        max_length=50, verbose_name="Título da demanda", help_text="Digite o título da demanda")
    data_inicial = models.DateField(verbose_name='Data de início')
    data_final = models.DateField(verbose_name='Data final')
    og = models.IntegerField(verbose_name="Ordem de grandeza")
   
    lista_de_atividades = models.ForeignKey(Atividade, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome)






#aluno/aluno

# Create your models here.

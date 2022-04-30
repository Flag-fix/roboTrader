from enum import Enum


class TipoPessoa(Enum):

    FISICA = "Física"
    JURIDICA = "Juridida"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class Prioridade(Enum):
    ALTA = "Alta"
    BAIXA = "Baixa"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Status(Enum):
    ABERTA = "Aberta"
    FECHADA = "Fechada"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Prioridade(Enum):
    ALTA = "Alta"
    BAIXA = "Baixa"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Status(Enum):
    ABERTA = "Aberta"
    FECHADA = "Fechada"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

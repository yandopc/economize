#!/usr/bin/env python

from Despesas import *
from Data import *

class Fixas (Despesas):
    def __init__ (vencimento:Data, categoria: Categoria, valor:float, descricao:str):
        Despesas.__init__(self, categoria, valor, descricao)
        self.__vencimento = vencimento

    @property
    def vencimento (self):
        return vencimento

    @vencimento.setter
    def vencimento (vencimento: Data):
        if isinstance (vencimento, Data):
            self.__vencimento = vencimento
        else:
            raise AttributeError

    def atualiza_informacoes (self):
        pass

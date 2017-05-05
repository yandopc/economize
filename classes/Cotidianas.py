#!/usr/bin/bash python

from Cotidianas import *
from Data import *

class Cotidianas (Despesas):
    def __init__ (self, vencimento: Data, categoria: Categoria, valor:float, descricao:str):
        Despesas.__init__ (self, categoria, valor, descricao)
        self.vencimento = vencimento

    @property
    def vencimento (self):
        return vencimento

    @vencimento.setter
    def vencimento (self, vencimento: Data):
        if isinstance (vencimento, Data):
            self.__vencimento = vencimento
        else:
            raise AttributeError

    

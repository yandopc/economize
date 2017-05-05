#!/usr/bin/env python

from Lancamento import *
from Data import *

class Receita (Lancamento):
    def __init__ (self, valor:float, descricao:str, data:Data):
        Lancamento.__init__(valor, descricao)
        self.__data = data

    @property
    def data (self):
        return data

    @data.setter
    def data (self, data: Data):
        if isinstance (data, Data):
            self.__data = data
        else:
            raise AttributeError

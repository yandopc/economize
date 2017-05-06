#!/usr/bin/env python

from Lancamento import *
from Data import *

class Receita (Lancamento):
    def __init__ (self, valor:float, descricao:str, data:Data = Data()):
        Lancamento.__init__(self, valor, descricao)
        self.data = data

    @property
    def data (self):
        return self.__data

    @data.setter
    def data (self, data: Data):
        if isinstance (data, Data):
            self.__data = data
        else:
            raise AttributeError

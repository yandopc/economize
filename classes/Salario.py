#!/usr/bin/env python

from Data import *

class Salario:
    def __init__ (self, data:Data, valor:float, descricao:str = ""):
        self.data = data
        self.valor = valor
        self.descricao = descricao

    @property
    def data (self):
        return self.__data

    @data.setter
    def data (self, data:Data):
		if isinstance (data, Data):
			self.__data = data
        else:
            raise AttributeError

    @property
    def descricao (self):
        return self.__descricao

    @descricao.setter
    def descricao (self, descricao:str):
		if isinstance (descricao, str):
			self.__descricao = descricao
        else:
            raise AttributeError

    @property
    def valor (self):
        return self.__valor

    @valor.setter
    def valor (self, valor:float):
		if isinstance (valor, float) or isinstance(valor, int):
			if valor >= 0:
                self.__valor = valor
            else:
                raise ValueError
        else:
            raise AttributeError

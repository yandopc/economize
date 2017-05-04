#!/usr/bin/env python

class Salario:
    def __init__ (self, data:str, valor:float = 0, descr:str = 0):
        self.__data = data
        self.__valor = valor
        self.__descricao = descr

    def atualizaSalario (self, valor:float):
        self.__valor = valor

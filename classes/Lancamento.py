#!/usr/bin/env python

class Lancamento:
    def __init__ (self, valor:float, descricao:str):
        self.valor = valor
        self.descricao = descricao

    @property
    def valor (self):
        return self.__valor

    @valor.setter
    def valor (self, valor:float):
        if isinstance (valor, float):
            self.__valor = valor
        else:
            print("Erro aqui")

    @property
    def descricao (self):
        return self.__descricao

    @descricao.setter
    def descricao (self, descricao:str):
        if isinstance (descricao, str)
            self.__descricao = descricao
        else:
            print("Erro aqui")

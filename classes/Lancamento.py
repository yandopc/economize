#!/usr/bin/env python

class Lancamento:
    #codigo = 0
    def __init__ (self, valor:float, descricao:str):
        #Lancamento.codigo += 1
        #self.__codigo = Lancamento
        self.valor = valor
        self.descricao = descricao

    @property
    def codigo (self):
        return self.__codigo

    @property
    def valor (self):
        return self.__valor

    @valor.setter
    def valor (self, valor:float):
        if isinstance (valor, float):
            self.__valor = valor
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

#!/usr/bin/env python

from Categoria import *
from Lancamento import *

class Despesas (Lancamento):
    def __init__ (self, categoria: Categoria, valor:float, descricao:str):
        #super (Despesas, self).__init__(valor, descricao)
        Lancamento.__init__(self, valor, descricao)
        self.__categoria = categoria

    @property
    def categoria (self):
        return (
            self.__categoria.nome,
            self.__categoria.descricao
            )

    @categoria.setter
    def categoria (self, categoria:Categoria):
        if isinstance (categoria, Categoria):
            self.__categoria = categoria
        else:
            raise AttributeError

    def view (self):
        return (
            self.__categoria.nome,
            self.valor,
            self.descricao
        )

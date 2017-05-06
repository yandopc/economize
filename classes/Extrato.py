#!/usr/bin/env python

#editei

from Conta import *

class Extrato:
    def __init__ (self, mes:str, codigo:int, conta:Conta):
        self.mes = mes
        self.codigo = codigo
        self.conta = conta

    @property
    def mes (self):
        return self.__mes

    @mes.setter
    def mes (self, mes:str):
        if isinstance (mes, str):
            self.__mes = mes
        else:
            raise AttributeError

	@property
    def codigo (self):
        return self.__codigo

    @codigo.setter
    def codigo (self, codigo:int):
        if isinstance (codigo, int):
            self.__codigo = codigo
        else:
            raise AttributeError

	@property
    def conta (self):
        return self.__conta

    @conta.setter
    def conta (self, conta:Conta):
        if isinstance (conta, Conta):
            self.__conta = conta
        else:
            raise AttributeError

    def extrato (self):
        return (
            self.__mes,
            self.__codigo,
            self.__conta
        )

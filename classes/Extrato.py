#!/usr/bin/env python

from Conta import *

class Extrato:
    def __init__ (self, mes:str, codigo:int, conta:Conta):
        self.__mes = mes
        self.__codigo = codigo
        self.__conta = conta

    @property
    def mes (self):
        return self.__mes

    @mes.setter
    def mes (self, mes:str):
        if isinstance (mes, str):
            self.__mes = mes
        else:
            print ("Erro")

    def extrato (self):
        return (
            self.__mes,
            self.__codigo,
            self.__conta
        )

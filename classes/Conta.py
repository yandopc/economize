#!/usr/bin/env python

class Conta:
    def __init__(self,numero:int, valorMinimo:float = 0.0, valorDesejavel:float = 0, saldo:float=0.0):
        self.__numero = numero
        self.__valorMinimo = valorMinimo
        self.__valorDesejavel = valorDesejavel
        self.__saldo = saldo

    @property
    def numero (self):
        return self.__numero

    @numero.setter
    def numero (self,numero:int):
        if isinstance (numero,int):
            self.__numero = numero
        else:
            raise AttributeError

    def valorMinimo (self, valorMinimo:float):
        self.__valorMinimo = valorMinimo

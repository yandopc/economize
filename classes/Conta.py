#!/usr/bin/env python

class Conta:
    num_contas = 0
    def __init__(self, valor_minimo:float = 0.0, valor_desejavel:float = 0, saldo:float=0.0):
        Conta.num_contas+=1
        self.__numero = Conta.num_contas
        self.valor_minimo = valor_minimo
        self.valor_desejavel = valor_desejavel
        self.saldo = saldo

    @property
    def numero (self):
        return self.__numero

    @property
    def valor_minimo(self):
        return self.__valor_minimo
    @valor_minimo.setter
    def valor_minimo (self, valorMinimo:float):
        if (isinstance (valor_minimo,int) or isinstance (valor_minimo,int)):
            if(valor_minimo > 0.0):
                self.__valor_minimo = valor_minimo
            else:
                raise ValueError
        else:
            raise AttributeError

    @property
    def valor_desejavel(self):
        return self.__valor_desejavel

    @valor_desejavel.setter
    def valor_desejavel(self, valor_desejavel:float):
    if (isinstance (valor_desejavel,int) or isinstance (valor_desejavel,int)):
        if (valor_desejavel > 0.0):
            self.__valor_desejavel = valor_desejavel
        else:
            raise ValueError
    else:
        raise AttributeError

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo (self, saldo:float):
    if (isinstance (saldo,int) or isinstance (saldo,int)):
        if(saldo > 0.0):
            self.__saldo = saldo
        else:
            raise ValueError
    else:
        raise AttributeError

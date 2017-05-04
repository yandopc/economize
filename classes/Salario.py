#!/usr/bin/env python

class Salario:
    def __init__ (self, data:str, valor:float = 0, descr:str = 0):
        self.__data = data
        if valor > 0:
            self.__valor = valor
        else:
            print ("Salário inválido")
        self.__descricao = descr

    @property
    def salario (self):
        return self.__valor

    @salario.setter
    def salario (self, salario:float):
        if isinstance (salario, float):
            self.__salario = salario
        else:
            print ("Tratar erro")

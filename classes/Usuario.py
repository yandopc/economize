#!/usr/bin/env python

from Conta import *
from Contato import *

class Usuario:
    def __init__(self, nome:str, senha:str = 0, contato:Contato = 0, contas:list = []):
        self.__nome = nome
        self.__senha = senha
        self.__contas = contas
        self.__contato = contato

    def __senha (self, senha:str):
        self.__senha = senha;
    '''
    @property
    def conta (self) -> list:
        return self.__contas

    @conta.setter
    def conta (self, conta:Conta):
        if isinstance (conta, Conta):
            self.__contas.append(conta)
        else:
            print("Tratar exceção")
    '''

    def atualizaDados (self):
        pass

    def excluirContas (self, conta:Conta):
        pass

    def transferir (self):
        pass

    @property
    def nome (self):
        return self.__nome
    @nome.setter
    def nome (self, nome:str):
        self.__nome = nome

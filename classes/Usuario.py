#!/usr/bin/env python

from Conta import *
from Contato import *

class Usuario:
    def __init__(self, nome:str, senha:str = 0, contato:Contato = 0, contas:list = []):
        self.__nome = nome
        self.__senha = senha
        self.__contas = contas
        self.__contato = contato

    def alteraSenha (self, senha:str):
        self.__senha = senha;

    def cadastrarConta (conta:Conta):
        self.__contas.append(conta)

    def atualizaDados ():
        pass

    def transferirContas ():
        pass

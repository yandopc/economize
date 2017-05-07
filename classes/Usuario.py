#!/usr/bin/env python

from Conta import *
from Contato import *

class Usuario:
    def __init__(self, nome:str, senha:str, contato:Contato, contas:list = []):
        self.__nome = nome
        self.__senha = senha
        self.contas = contas
        self.contato = contato
"""
    def __senha (self, senha:str):
        self.__senha = senha;
"""
    @property
    def contas (self):
        return self.__contas

	def add_conta(self, conta:Conta):
		if isinstance (conta, Conta):
            self.__contas.append(conta)
        else:
            raise AttributeError

    """@contas.setter
    def contas (self, conta:Conta):
        if isinstance (conta, Conta):
            self.__contas.append(conta)
        else:
            raise AttributeError
"""
    def atualiza_dados (self):
        pass

    def excluir_contas (self, conta:Conta):
        pass

    def transferir (self):
        pass

    @property
    def nome (self):
        return self.__nome
    @nome.setter
    def nome (self, nome:str):
        if isinstance (nome, str):
            self.__nome = nome
        else:
            raise AttributeError

    @property
    def contato (self):
        return (
            self.__contato.email,
            self.__contato.telefone
            )

    @contato.setter
    def contato (self, contato:Contato):
        if isinstance (contato, Contato):
            self.__contato = contato
        else:
            raise AttributeError

	@staticmethod
	def varifica_usuario(pessoa:Usuario, email:str, senha:str):
		if pessoa.contato[0] == email :
			if pessoa.senha == senha :
				return True
			else:
				return NameError("Senha invalida!")
		else:
			return NameError("Email invalido!")

	@staticmethod
	def permissao_sistema(email:str, senha:str, usuarios:list):
		for usuario in usuarios:		
			if usuario.contato[0] == email and pessoa.senha == senha :
				return usuario
		return None







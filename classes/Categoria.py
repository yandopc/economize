#!/usr/bin/env python

class Categoria(object):
	def __init__(self, nome:str, descricao:str=""):
		self.nome = nome
		self.descricao = descricao
	@property

	def nome (self):
		return self.__nome

	@nome.setter
	def nome (self, nome):
		if isinstance(nome, str):
			self.__nome = nome
		else:
			raise AttributeError

	@property
	def descricao (self):
		return self.__descricao

	@descricao.setter
	def descricao (self, descricao):
		if isinstance(descricao, str):
			self.__descricao=descricao
		else:
			raise AttributeError

	def __str__ (self):
		return (self.__nome, self.__descricao)

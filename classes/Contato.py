#!/usr/bin/env python

class Contato:
    def __init__ (self, telefone:str, email:str):
        self.__telefone = telefone;
        self.__email = email

    def alteraEmail (self, email:str):
        self.__email = email

''#!/usr/bin/env python

def testa_email (email:str):
    if '@' in email:
            return True
    return False

class Contato:
    def __init__ (self, telefone:str, email:str):
        self.telefone = telefone;
        self.email = email

    @property
    def email (self):
        return self.__email

    @email.setter
    def email (self, email:str):
        if isinstance (email, str) and testa_email(email):
            self.__email = email
        else:
            print ("Tratar erro")

    @property
    def telefone (self):
        return self.__telefone

    @telefone.setter
    def telefone (self, telefone:str):
        if isinstance (telefone, str):
            self.__telefone = telefone
        else:
            print ("Tratar erro")

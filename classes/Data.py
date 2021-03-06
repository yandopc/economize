#!/usr/bin/env python

from datetime import *
#str(hj.day)+"/"+str(hj.month)+"/"+str(hj.year)
class Data:
    def __init__(self, dia:int = date.today().day, mes:int = date.today().month, ano:int = date.today().year):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @property
    def dia (self):
        return self.__dia
        
    @dia.setter
    def dia (self, dia:int):
        if isinstance (dia, int):
            if (dia > 0 and dia <= 31):
                self.__dia = dia
            else:
                raise ValueError
        else:
            raise AttributeError

    @property
    def mes (self):
        return self.__mes

    @dia.setter
    def mes (self, mes:int):
        if isinstance (mes, int):
            if (mes > 0 and mes <= 12):
                self.__mes = mes
            else:
                raise ValueError
        else:
            raise AttributeError

    @property
    def ano (self):
        return self.__ano

    @ano.setter
    def ano (self, ano:int):
        if isinstance (ano, int):
            if (ano > 0):
                self.__ano = ano
            else:
                raise ValueError
        else:
            raise AttributeError

    def __gt__(self, other):
        if (self.ano == other.ano):
            if (self.mes == other.mes):
                if (self.dia == other.dia or self.dia < other.dia):
                    return False
                else:
                    return True
            elif (self.mes < other.mes):
                return False
            else:
                return True
        elif (self.ano < other.ano):
            return False
        else:
            return True

    def __lt__(self, other):
        if (self.ano == other.ano):
            if (self.mes == other.mes):
                if (self.dia == other.dia or self.dia > other.dia):
                    return False
                else:
                    return True
            elif (self.mes > other.mes):
                return False
            else:
                return True
        elif (self.ano > other.ano):
            return False
        else:
            return True

    def __eq__(self, other):
        if (self.dia == other.dia and self.mes == other.mes and self.ano == other.ano):
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.dia != other.dia or self.mes != other.mes or self.ano != other.ano):
            return True
        else:
            return False

    def __str__ (self):
        return str(self.dia)+"/"+str(self.mes)+ "/" + str(self.ano)

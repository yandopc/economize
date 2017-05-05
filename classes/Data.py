from datetime import *
#str(hj.day)+"/"+str(hj.month)+"/"+str(hj.year)
class Data:
    def __init__(self, dia:int=date.today().day, mes:int, ano:int):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @property
    def dia (self):
        return self.__dia
    @dia.setter
    def dia (self,dia:int):
        if(isinstance (dia:int)):
            if(dia >0 && dia <=31):
                self.__dia = dia
            else:
                raise ValueError
        else:
            raise AttributeError

    @property
    def mes(self):
        return self.__mes
    @dia.setter
    def mes(self,mes:int):
        if(isinstance (mes:int)):
            if(mes >0 && mes <=12):
                self.__mes = mes
            else:
                raise ValueError
        else:
            raise AttributeError

    @property
    def ano(self):
        return self.__ano
    @dia.setter
    def ano(self,ano:int):
        if(isinstance (ano:int)):
            if(ano >0):
                self.__ano = ano
            else:
                raise ValueError
        else:
            raise AttributeError

    def __gt__(self,other):
        if(self.ano == other.ano):
            if(self.mes == other.mes):
                if(self.dia == other.dia or self.dia < other.dia):
                    return False
                else:
                    return True
            elif(self.mes < other.mes):
                return False
            else:
                return True
        elif(self.ano < other.ano):
            return False
        else:
            return True

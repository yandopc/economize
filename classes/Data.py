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

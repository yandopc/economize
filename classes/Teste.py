from Conta import *

conta = Conta(123)
try:
    conta.numero = 2
    conta.numero = 3.0
except(AttributeError):
    print("Erro de atributo")
print(conta.numero)

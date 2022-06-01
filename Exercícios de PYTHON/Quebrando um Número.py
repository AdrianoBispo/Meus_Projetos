# Quebrando um Número 

#   Método Generalizado
import math
num = float(input('Digite um valor: '))
inteiro = math.trunc(num)
print('Seu valor é {} e sua forma interia é {}'.format(num, inteiro))


#   Método Específico
from math import trunc
num = float(input("Digite um valor: "))
inteiro = trunc(num)
print('O valor digitado é igual a {} e o seu valor inteiro é {}'.format(num, inteiro))

#   Método sem o comando Import
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
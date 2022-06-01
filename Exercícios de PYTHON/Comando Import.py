# Utilizando Import:
# O 'import' ele trás o acesso a todos os itens de uma biblioteca.

# Exemplo:

#Esse é Generalizado:
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# Esse é Específico:
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))


# No 'python.org' - > 'PyPi' == Bibliotecas Externas
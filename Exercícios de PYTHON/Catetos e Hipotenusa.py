# Catetos e Hipotenusa

# Método realizado por mim
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = (co ** 2) + (ca ** 2)
hipotenusa = h ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

# Método sem Import do Guanabara
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Método utilizando o Import
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot (co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
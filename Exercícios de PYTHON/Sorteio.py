# Sorteando um item da lista
#import random
#aluno1 = str(input('Primeiro Aluno: '))
#aluno2 = str(input('Segundo Aluno: '))
#aluno3 = str(input('Terceiro Aluno: '))
#aluno4 = str(input('Quarto Aluno: '))
#lista = [aluno1, aluno2, aluno3, aluno4]
#print('O aluno escolhido foi {} !'.format(random.choice(lista)))

# Sorteando uma Ordem da Lista
import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo Aluno: '))
c = str(input('Terceiro Aluno: '))
d = str(input('Quarto Aluno: '))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
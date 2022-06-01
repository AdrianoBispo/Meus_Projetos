#     OPERADORES ARITMÉTICOS

# Ordem de Precedência

# 1°{()} As operações dentro dele são calculados 1°
# 2°(**) Exponeciação 
# [n ** (1/2), (1/3) ...] -> Raiz Quadrada, Raiz Cubica ...
# 3° (/) Divisão compatível com decimal
# 3° (//) Divisão apenas com resultado Inteiro
# 3° (%) Resto da Divisão
# 3° (*) Multiplicação
# 4° (+) Adição
# 4° (-) Subtração

#    CURIOSIDADE

# 'Oi' + 'Olá' = 'OiOlá' (Contatenação)
# 'Oi' * 5 = "OiOiOiOiOi" (Oi 5x)
# '=' * 20 = (= 20x)

#  Parte 1 da Aula

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))

#{:20} -> O nome terá o espaço de 20caracteres

print('Prazer em te conhecer {:>20}!'.format(nome))

#{:>20} -> O nome terá 20caracteres à direita

print('Prazer em te conhecer {:<20}!'.format(nome))

#{:<20} -> O nome terá 20caracteres à esquerda

print('Prazer em te conhecer {:^20}!'.format(nome))

#{:^20} -> O nome terá 20caracteres e será centralizado

print('Prazer em te conhecer {:=^20}!'.format(nome))

#{:=^20} -> O nome terá 20caracteres, ao seu redor terá o sinal de [=]

# PARTE 2 da Aula

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}'.format(n1 + n2))
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))

# {:.3f} -> limita até a 3 casa decimal

print('Divisão inteira é {}\n A potência é {}'.format(di, e))

#{\n} -> Divide o código de mesma linha colocando-o na linha abaixo

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')

#{end=' '} -> Une o código da linha atual com o código da linha abaixo

print('A divisão inteira é {} e a potência é {}'.format(di, e))
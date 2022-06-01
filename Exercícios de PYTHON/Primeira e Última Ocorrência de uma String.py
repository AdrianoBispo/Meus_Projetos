#  Primeira e Última Ocorrência de uma String

frase = str(input('Digite uma Frase: ').split())
f = frase.upper()
print('A letra A aparecerá {}x na frase.'.format(f.count('A')))
print('A primeira letra A apareceu na {}'.format(f.find('A')))
print('A última letra A apareceu {}'.format(f.rfind('A')))

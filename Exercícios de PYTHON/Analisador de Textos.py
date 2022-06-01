# Analisador de Textos

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu prieiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
# Condições (parte 1)

# nome = str(input('Qual é o seu nome? '))
# if nome == 'Gustavo':
    # print('Que nome lindo você tem!')
# else:
    # print('Seu nome é tão comum!')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite sue segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
# if m >= 6.0:
    # print('Sua média foi boa! Parabéns!')
# else:
    # print('Sua média foi ruim! Estude mais!')
print('PARABÉNS!!!' if m >= 6.0 else 'ESTUDE MAIS!' )
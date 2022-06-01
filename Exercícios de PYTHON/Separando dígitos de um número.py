# Separando dígitos de um número

n = int(input('Informe um número: '))
num = str(n)
print('Analisando o número:', n)
print('Unidade:', num[3])
print('Dezena:', num[2])
print('Centena:', num[1])
print('Milhar:', num[0])
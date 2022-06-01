# Aluguel de Carros

aluguel = int(input('Quantos dias alugados ? '))
rodados = int(input('Quantos Km rodados ? '))
cálculo = (aluguel * 60) + (rodados * 0.15)
print('O total a pagar é R${:.2f}'.format(cálculo))
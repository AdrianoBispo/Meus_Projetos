# Reajuste Salarial

funcionário = float(input('Qual é o salário do Funcionário ? R$'))
aumento = (funcionário * 15 / 100)
salario = funcionário + aumento
print('O funcionário que ganhava R${}, com o 15% de aumento, passa a receber R${}.'.format(funcionário, salario))

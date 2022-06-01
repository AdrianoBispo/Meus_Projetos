# Meu Conversor de Moedas

Reais = float(input('Quantos reais você tem na carteira ? '))
Dólar = Reais / 4.65
Euro = Reais / 5.02
print('Com {:.2f} reais você pode comprar {:.2f} dólares ou {:.2f} euros.'.format(Reais, Dólar, Euro))
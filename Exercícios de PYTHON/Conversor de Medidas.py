# Meu Conversor de Medidas

distância = int(input('Digite um valor: '))

print('Seu valor em metros é {}m'.format(distância))
print('A medida de {} em Km é {}'.format(distância, distância / 1000))
print('A medida de {} em hm é {}'.format(distância, distância / 100))
print('A medida de {} em dam é {}'.format(distância, distância / 10))
print('A medida de {} em dm é {}'.format(distância, distância * 10))
print('A medida de {} em cm é {}'.format(distância, distância * 100))
print('A medida de {} em mm é {}'.format(distância, distância * 1000))

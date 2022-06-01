# Calculadora de Tinta para Parede

Largura = float(input('Quantos metros tem a largura da parede ? '))
Altura = float(input('Quantos metros tem a altura da parede ? '))
dimensão = '{}x{}'.format(Largura, Altura)
área = Largura * Altura
tinta = área / 2
print('Sua parede tem a dimensão de {} e sua área é de {}m².'.format(dimensão,área))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
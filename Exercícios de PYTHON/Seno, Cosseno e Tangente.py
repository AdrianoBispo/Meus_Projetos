# Seno, Cosseno e Tangente
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(ângulo))
c = math.cos(math.radians(ângulo))
t = math.tan(math.radians(ângulo))
print('O seno do ângulo {} é {:.2f}'.format(ângulo, s))
print('O cosseno do ângulo {} é {:.2f}'.format(ângulo, c))
print('O tangente do ângulo {} é {:.2f}'.format(ângulo, t))
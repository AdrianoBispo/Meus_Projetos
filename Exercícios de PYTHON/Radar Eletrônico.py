# Radar Eletrônico

velocidade = int(input('Velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de velocidade que é de 80km/h\nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
    
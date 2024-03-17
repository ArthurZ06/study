velocidade =float(input('Qual é a velocidade atual do carro?' .strip()))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido da via que é de 80Km/h' )
    multa = (velocidade-80) * 7
    print('Você devera pagar uma multa de R${:.2f}! '.format(multa))
else:
    print('Você é um ótimo cidadão meus parabéns :)' )

peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f} '.format(imc))

if imc < 18.5:
    print('Abaixo do peso ')
    print('Meu brother tu é muito magro tá poxa filho ')
elif imc <= imc < 25:
    print('Peso ideal')
    print('Você é muito saúdavel me passa esse formula por favor ')
elif imc <= imc < 30:
    print('Sobrepeso')
    print('Já está na hora de emagracer você não acha? ')
elif imc <= imc < 40:
    print('Obesidade')
    print('Você está muito gordo pelo amor de deus vai emagrecer meu filho ')
elif imc <= imc < 40:
    print('Obesidade mórbida')
    print('O que você espera que vai acontecer na sua vida com esse tanto de banha?')



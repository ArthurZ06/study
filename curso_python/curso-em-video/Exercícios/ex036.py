casa = float(input('Qual é o valor da casa? R$ '.strip()))
salario = float(input('Quanto você ganha por mês? R$ '.strip()))
anos = int(input('Quantos anos você quer pagar essa casa? R$ '.strip()))
prestação = casa / (anos * 12)
mínimo = (salario * 30 / 100)

print('para pagar a casa de R${:.2f} em {} anos'.format(casa, anos))
print('a prestação será de R${:.2f}'.format(prestação))

if prestação <= mínimo:
    print('O emprestimo pode ser concedido ')
else:
    print('o emprestivo foi negado')

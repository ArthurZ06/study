salario = float(input('Salario inicial:'.strip()))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Seu novo salario vai ser {}'.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Seu novo salario vai ser {:.2f}'.format(novo))

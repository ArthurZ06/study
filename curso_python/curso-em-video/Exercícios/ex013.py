salario =float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${},com 15% de aumento,passara a receber  R${}'.format(salario, novo))


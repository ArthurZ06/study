num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '.strip()))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '.strip()))
print('Você digitou {} números é a soma dos números foram {}'.format(cont, soma))


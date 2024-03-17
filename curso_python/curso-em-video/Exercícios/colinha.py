#num = [2, 5, 9, 1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 2)
#if 4 in num:
#    num.remove(4)
#else:
#    print('Não achei o número 5')
#num.remove(2)
#num.pop(2)
#print(num)
#print(f'Essa lista tem {len(num)} elementos')
#################################################
#valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)

#for v in valores:
#   print(f'{v}...')

#valores = list()
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor ')))

#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontre o valor {v}!')
#print('Cheguei ao final da lista.')

#valores = list()
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))
#########################################################
a = [2, 3, 4, 7]
#b = a #Cria uma ligação entre elas
b = a[:]# Cria uma copia da lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
lista = list()
pares = list()
impas = list()
while True:
    lista.append(int(input('Digite um número: ')))
    prox = str(input('Quer continuar? [S/N]')).upper()
    if prox == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impas.append(v)
print('+' * 30)
print(f'A lista completa é {lista} ')
print(f'A lista de pares é {pares} ')
print(f'A lista de ímpares é {impas}')
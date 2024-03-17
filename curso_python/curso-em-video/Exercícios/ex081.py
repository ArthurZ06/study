lista = []
cinco = 0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    lista.sort(reverse=True)
    resp = str(input('Quer continuar? [S/N]')).upper()
    if n == 5:
        cinco += 1
    if resp == 'N':
        break
print(f'Essa lista tem {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista} ')
print(f'O valor 5 foi encontrado {cinco} ')


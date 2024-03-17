dados = list()
pessoas = list()
cont = maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    cont += 1
    dados.append(peso)
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    prox = str(input('Quer continuar? [S/N] ')).upper()
    if prox in 'N':
        break
print('=' * 40)
print(f'Ao todo,Você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior}Kg.Pesso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}Kg.Pesso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()

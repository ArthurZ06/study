print('=' * 30)
print('     LOJA SUPER BARATÃO')
print('=' * 30)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
        barato = produto
#   Simplificado
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
#   Sem ser Simplificado
#    else:
#        if preço < menor:
#           menor = preço
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar?')).upper().strip()[0]
    if r == 'N':
        break
print(f'O total de compra foi R${total}')
print(f'Temos {totmil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))

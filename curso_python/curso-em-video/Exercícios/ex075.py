escolha = '1'
while escolha == '1':
    print('-=' * 40)
    num = (int(input('Dite um valor:')),
           int(input('Digite outro valor:')),
           int(input('Digite mais um valor:')),
           int(input('Digite o ultimo valor:')))
    print(f'Os numeros digitados são: ', end='')
    for c in num:
        print(f'{c}', end=' ')
    print('\nOs numeros pares são:', end=' ')
    for par in num:
        if par % 2 == 0:
            print(par, end=' ')
    localisasao = int(input('\nDigite o valor que você deseja localizar:'))
    while localisasao not in num:
        localisasao = int(input('Você deve digitar um valor que você já tenha digitado:'))
    print(f'O numero {localisasao} se encontra na {num.index(localisasao) + 1}º posição ')
    cont = ' '
    while cont not in num:
        cont = int(input('digite um valor que você queira saber quantas vezes você digitou:'))
    print(f'O numero {cont} apareceu {num.count(cont)} vez')
    print('''[ 1 ] Digitar e analisar novos numeros
[ 2 ] Encerrar o programa''')
    escolha = '5'
    while escolha not in '1 2':
        escolha = str(input('Qual a sua opição:'))
    if escolha == '2':
        break
print('>>>>>>>>>> FIM DO PROGRAMA <<<<<<<<<<')


from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''-----------------------------
[ 1 ] somar 
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novo números
[ 5 ] sair do programa
-----------------------------''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(soma)
    elif opção == 2:
        multi = n1 * n2
        print(multi)
    elif opção == 3:
        if n1 > n2 == n2:
            print('Entre {} é {} o maior valor é {} '.format(n1, n2, n1))
        else:
            print('Entre {} é {} o maior valor é {} '.format(n1, n2, n2))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente ')

print('Fim do programa! Volte sempre! ')


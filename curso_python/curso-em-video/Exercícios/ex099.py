def linha():
    print('-=' * 20)


def maior(*num):
    from time import sleep
    linha()
    c = 0
    print("Analisando os valores recebidos...")
    for c in num:
        sleep(.25)
        print(f'{c} ', end='')
        c += 1
    print(f'Foram infomados {c} valores.')
    if len(num) == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(num)}.')
    sleep(2)

# Parte principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

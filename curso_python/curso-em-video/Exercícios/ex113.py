def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mInfelismente tivemos um problema :(\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO: por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digiter esse número.\033[m')
            return 0
        else:
            return n


n = leiaInt(('Digite um número Inteiro: '))
nr = leiaFloat('Digite um número Real: ')
print(f'\033[0;36mO valor inteiro digitado foi {n} e o real foi {nr}\033[m')
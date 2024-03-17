from random import randint
v = d = 0
print('\033[33m=-' * 15)
print('\033[33mVAMOS JOGAR PAR OU ÍMPAR ')
print('\033[33m=-' * 15)
nome = str(input('\033[33mQual é o seu nome? '.strip()))
while True:
    jogador = int(input('\033[33mDigite um valor: '.strip()))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[33mPar ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'você jogou {jogador} é o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'\033[34mparabéns {nome} você ganhou a primeira rodada 😎😎😎 mais a proxima você não me escapa ')
            v += 1
        else:
            print(f'\033[31mHiii {nome} você PERDEU! muito ruim 😂😂😂 ')
            d += 1
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'\033[34mparabéns {nome} você ganhou a primeira rodada 😎😎😎 mais o proxima você não me escapa ')
            v += 1
        else:
            print(f'\033[31mHiii {nome} você PERDEU! muito ruim 😂😂😂 ')
            d += 1
            break
        print(f'Vamos jogar novamente {nome}')
    else:
        if v > d:
            print('Ainda sou o melhor do pedaço 😂😂😂')
        else:
            print('Você é o melhor do pedaço 😎😎😎')
    print(f'Você ganhou {v} é perdeu {d}')

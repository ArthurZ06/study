from random import choice
from time import sleep
c = choice(['PEDRA 👊', 'PAPEL 🖐', 'TESOURA ✌'])
o = ['']

print('=' * 16)
print('👊🖐 ✌ JOGO DO JOKENPÔ 👊🖐 ✌')
print('=' * 16)
sleep(1)
print('Escolha entre:\n[1] - PEDRA 👊\n[2] - PAPEL 🖐\n[3] - TESOURA ✌')
print('=' * 16)
print('')
e = int(input(f'Digite: '))
print('')
sleep(0.3)

if e == 1:
    o = 'PEDRA 👊'
    print(f'Você escolheu {o} e o computador escolheu {c}')
    if o == c:
        print(f'EMPATOU!')
    elif c == 'PAPEL 🖐':
        print('Você PERDEU!')
    else:
        print('você GANHOU!')
elif e == 2:
    o = 'PAPEL 🖐'
    print(f'Você escolheu {o} e o computador escolheu {c}')
    if o == c:
        print(f'EMPATOU!')
    elif c == 'TESOURA ✌':
        print('você PERDEU!')
    else:
        print('Você GANHOU!')
elif e == 3:
    o = 'TESOURA ✌'
    print(f'Você escolheu {o} e o computador escolheu {c}')
    if o == c:
        print('EMPATOU!')
    elif c == 'PEDRA 👊':
        print('Você PERDEU!')
    else:
        print('Você GANHOU!')
else:
    print('OPÇÃO INVÁLIDA!')
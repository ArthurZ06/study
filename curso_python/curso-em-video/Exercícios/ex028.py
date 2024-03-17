from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5.Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('em que número eu pensei? '.strip()))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns você ganhou de mim ')
else:
    print('Hi muito ruim perdeu troxa')

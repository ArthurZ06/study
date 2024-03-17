from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('JOGA NA MEGA SENA'.center(30))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 100)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('FIM DO PROGRAMA'.center(30))

#Pretendo terminar o programa do meu jeito 

#from random import randint
#from time import sleep
#mega_sena = []
#jogos = []
#cont = 0
#print('-' * 30)
#print('      JOGA NA MEGA SENA      ')
#print('-' * 30)
#sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
#print('-=' * 3, f'SORTEANDO {sorteio} JOGOS', '-=' * 3)
#while True:
#    num = randint(1, 100)
#    if num not in mega_sena:
#        mega_sena.append(num)
#        cont += 1
#    if cont >= 6:
#        break
#mega_sena.sort()
#jogos.append(mega_sena[:])
#mega_sena.clear()
#for c in range(sorteio+1):
#    print(f'Jogo {c}: {jogos}')
#sleep(1)
from time import sleep


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg} ')
    print('~' * tam)


def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, '', end='')
        sleep(0.5)
    print()


escreva('Contagem de 1 até 10 de 1 em 1 ')
contagem(1, 10, 0)
print()
escreva('Contagem de 10 até 0 de 2 em 2 ')
contagem(10, 0, 2)
contagem(int(input('Inicio: ')), int(input('Fim:')), int(input('Passo: ')))

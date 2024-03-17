print('\033[34m-' * 30)
print('Seguência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '.strip()))
t1 = 0
t2 = 1
cont = 2
print('~' * 30)
print('{} ↦ {} '.format(t1, t2), end='')

while cont <= n:
    t3 = t1 + t2
    print(' ↦ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ↦ Fim')

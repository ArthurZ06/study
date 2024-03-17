n = int(input('Digite um número: '.strip()))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[35mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('\033[33mÉ por isso ele É PRIMO! ')
else:
    print('\033[33mÉ por isso ele NÃO É PRIMO! ')
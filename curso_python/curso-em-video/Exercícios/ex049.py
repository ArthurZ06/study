num = int(input('Digite um número para ver a tabuada: '.strip()))
for c in range(0, 11):
    print('{} x {} = {} '.format(num, c, num * c))

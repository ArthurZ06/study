num =int(input('Me diga um número qualquer: '.strip()))
resultado = num % 2
if resultado ==0:
    print('O número {} é impar '.format(num))
else:
    print('O número {} é pár '.format(num))
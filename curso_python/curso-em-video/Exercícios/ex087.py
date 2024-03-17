matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = s = t = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor: [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            p += matriz[l][c]
for l in range(0, 3):
    s += matriz[l][2]
for c in range(0, 3):
    if c == 0 or matriz[1][c] > t:
        t = matriz[1][c]
print(f'A soma dos valores pares é {p}')
print(f'A soma dos valores da terceira coluna é {s}')
print(f'O maior valor da segunda linha é {t}')

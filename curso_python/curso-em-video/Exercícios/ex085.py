junto = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        junto[0].append(num)
    else:
        junto[1].append(num)
print('=' * 30)
junto[0].sort()
junto[1].sort()
print(f'Os valores dos pares digitados foram: {junto[0]}')
print(f'Os valores dos ímpares digitados foram: {junto[1]}')
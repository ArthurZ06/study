num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

#FORMA 1:

def maior(num1, num2, num3):
    max = num1

    if num3 > max:
        max = num3
    if num2 > max:
        max = num2

    return max

def menor(num1, num2, num3):
    min = num1

    if num2 < min:
        min = num2
    if num3 < min:
        min = num3

    return min

print(f'O maior é {maior(num1, num2, num3)}')

print(f'O menor é {menor(num1, num2, num3)}')


resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('\033[34mDigite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar: [S/N] '.strip())).upper()
media = soma / quant
print('Você digitou {} número e a média foi {} '.format(quant, media))
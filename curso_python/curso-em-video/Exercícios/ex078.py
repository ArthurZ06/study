valores = []
p1 = p2 = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
p1 += valores.index(max(valores))
p2 += valores.index(min(valores))
print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições {p1}')
print(f'O menor valor digitado foi {min(valores)} nas posições {p2}')

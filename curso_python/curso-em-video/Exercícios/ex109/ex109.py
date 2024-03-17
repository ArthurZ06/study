import moeda

p = int(input('Digite o preço: '))
dobro = moeda.dobro(p, True)
metade = moeda.metade(p, True)
aumento = moeda.aumentar(p, 10, True)

print(f'A metade de {p} é {metade}')
print(f'O dobro de {p} é {dobro}')
print(f'O aumento de {p} é {aumento}')

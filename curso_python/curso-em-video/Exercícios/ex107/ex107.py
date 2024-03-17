import moeda

p = int(input('Digite o preço: '))
dobro = moeda.dobro(p)
metade = moeda.metade(p)
aumento = moeda.aumento(p)

print(f'A metade de {p} é {metade}')
print(f'O dobro de {p} é {dobro}')
print(f'O aumento de {p} é {aumento}')

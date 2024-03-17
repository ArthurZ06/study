import moeda

p = int(input('Digite o preço: '))
dobro = moeda.moeda(moeda.dobro(p))
metade = moeda.moeda(moeda.metade(p))
aumento = moeda.moeda(moeda.aumentar(p, 10))

print(f'A metade de {p} é {metade}')
print(f'O dobro de {p} é {dobro}')
print(f'O aumento de {p} é {aumento}')

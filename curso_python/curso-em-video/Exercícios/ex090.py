dicionario = {}
lista = list()
dicionario['Nome'] = str(input('Nome: '))
dicionario['média'] = float(input(f'Média de {dicionario["Nome"]}: '))
lista.append(dicionario.copy())
print(f' - Nome é igual a {lista[0]["Nome"]}')
print(f' - Média é igual a {lista[0]["média"]}')
if lista[0]['média'] < 5.00:
    print(' - Situação é igual a Reprovado')
else:
    print(' - Situação é igual a Aprovado')

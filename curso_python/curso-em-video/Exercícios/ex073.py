lista = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'atheletico-PR', 'Atlético-MG', \
    'Fortaleza ', 'São Paulo ', 'América-MG ', 'Botafogo ', 'Santos ', 'Goiás ', 'Bragantino ', 'Coritiba ', \
    'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')

print('-=' * 30)
print(f'Lista de times do Brasileirão: {lista}')
print('-=' * 30)
print('Os 5 primeiro são ', lista[0:5])
print('-=' * 30)
print('Os 4 últimos são ', lista[-4:])
print('-=' * 30)
print('Times em ordem alfabética:', sorted(lista))
print('-=' * 30)
print('O', lista[8], 'está na 8 posição')

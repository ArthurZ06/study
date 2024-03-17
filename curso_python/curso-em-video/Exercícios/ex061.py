print('=' * 34)
print('       10 TERMOS DE UMA PA ')
print('=' * 34)
primeiro = int(input('Primeiro termo: '.strip()))
razão = int(input('Razão: '.strip()))
termo = primeiro
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' ↦ ')
    termo += razão
    cont += 1
print('Fim')


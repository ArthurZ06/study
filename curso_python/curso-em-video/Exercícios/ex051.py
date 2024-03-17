print('=' * 34)
print('       10 TERMOS DE UMA PA ')
print('=' * 34)

primeiro = int(input('Primeiro termo: '.strip()))
razão = int(input('Razão: '.strip()))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' ↦ ')
print('ACABOU')




print('=' * 22)
print('    Gerador de PA')
print('=' * 22)
primeiro = int(input('Primeiro termo: '.strip()))
razao = int(input('Razão da PA: '.strip()))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' ↦ ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '.strip()))
print('Progressão finalizada com {} termos mostrados. '.format(total))
print('Fim')

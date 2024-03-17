c = m = f = p = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '.strip()))
    sexo = str(input('Sexo: '.strip())).upper()[0]
    print('-' * 25)
    cont = str(input('Quer contunuar? [S/N]')).upper().strip()[0]
    if sexo in 'Ff' and idade < 20:
        f += 1
    if sexo in 'M':
        m += 1
    if idade < 18 and sexo in 'MF':
        p += 1
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {p} ')
print(f'Ao todo temos {m} homens cadastrados ')
print(f'E temos {f} mulheres com menos de 20 anos ')

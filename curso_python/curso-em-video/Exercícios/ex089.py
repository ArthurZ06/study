lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar? ')).upper()
    if r == 'N':
        break
print('-' * 26)
print(f'{"Nu.":<4}{"NOME":<10}{"MÉDIA":>8} ')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f} ')
while True:
    print('-' * 35)
    opc = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FIM DO PROGRAMA')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<<                VOLTE SEMPRE                >>>')

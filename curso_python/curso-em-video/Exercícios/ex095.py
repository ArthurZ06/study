jogador = {}
gol = []
analise = []
while True:
    print('-' * 51)
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou? '))
    for i in range(partidas):
        gol.append(int(input(f'Quantos gols na partida {i}: ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    analise.append(jogador.copy())
    gol.clear()
    while True:
        r = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        print(f'ERRO! Por favor, digite somente S ou N.')
    if r == 'N':
        break
print('-'*51)
print(f'{"COD":<5}{"NOME":<20}{"GOLS":<15}{"TOTAL":>10}')
print('-'*51)
for pos, d in enumerate(analise):
    gols = str(d["gols"])
    print(f'{pos:<5}{d["nome"]:<20}{gols:<15}{d["total"]:>7}', end='')
    print()
while True:
    print('-' * 51)
    op = int(input('Digite o código para ver os dados do jogador [999 para sair]: '))
    if op != 999:
        if op > len(analise)-1:
            print(f'ERRO! Não existe jogador com código {op}! Tente Novamente...')
        else:
            for pos, d in enumerate(analise):
                if op == pos:
                    print(f'→ LEVANTAMENTO DO JOGADOR {d["nome"]}')
                    for j, g in enumerate(d["gols"]):
                        print(f'  No jogo {j} fez {g} gols')
    else:
        print('FINALIZADO!')
        break
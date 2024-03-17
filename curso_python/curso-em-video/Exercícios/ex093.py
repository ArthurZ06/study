full = dict()
partidas = []
full['nome'] = str(input("nome do jogador: "))
full['partidas'] = int(input(f"Quantas partidas {full['nome']} jogou? "))
for c in range(full['partidas']):
    partidas.append(int(input(f'Quantos gols na {c} partida? ')))
full['gols'] = partidas[:]
full['total'] = sum(partidas)
print('-=' * 35)
print(full)
print('-=' * 35)
for k, v in full.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {full["nome"]} jogou {full["partidas"]} partidas.')
print('-=' * 20)
for i, v in enumerate(full['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {full["total"]} gols.')

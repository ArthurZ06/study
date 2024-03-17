Valores = [int(input('Digite um valor: '))]
print(f'Adicionado ao final da lista')
for c in range(0, 4):
    Valor = int(input('Digite um valor: '))
    if Valor >= max(Valores):
        Valores.insert(len(Valores), Valor)
        print(f'Adicionado ao final da lista')
    else:
        for p, v in enumerate(Valores):
            if Valor <= v:
                Valores.insert(p, Valor)
                print(f'Adicionado na posição {p} da lista')
                break
print('-='*35)
print(f'Os valores digitados em ordem foram {Valores}')

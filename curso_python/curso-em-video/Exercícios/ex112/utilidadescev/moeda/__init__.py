def metade(n1=0, formato=False):
    r = n1 / 2
    return r if formato is False else moeda(r)


def dobro(n1=0, formato=False):
    r = n1 * 2
    return r if formato is False else moeda(r)


def aumentar(n1=0, taxa=20, formato=False):
    r = n1 + (n1 * taxa/100)
    return r if formato is False else moeda(r)


def diminuir(n1=0, taxa=12, formato=False):
    r = n1 - (n1 * taxa/100)
    return r if formato is False else moeda(r)


def moeda(n1=0, moeda='R$'):
    return f'{moeda}{n1:.2f}'.replace('.', ',')


def resumo(p, taxa1, taxa2):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'preço analisado: \t{p}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'20% de aumento: \t{aumentar(p, taxa1, True)}')
    print(f'12% de redução: \t{diminuir(p, taxa2, True)}')
    print('-' * 30)

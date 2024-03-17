def metade(n1=0, resp=0):
    resp = n1 / 2
    return resp


def dobro(n1=0, r=0):
    r = n1 * 2
    return r


def aumentar(n1=0, taxa=0, resposta=0):
    resposta = n1 + (n1 * taxa/100)
    return resposta


def diminuir(n1=0, taxa=0, resp=0):
    resp = n1 - (n1 * taxa/100)


def moeda(n1=0, moeda='R$'):
    return f'{moeda}{n1:.2f}'.replace('.', ',')

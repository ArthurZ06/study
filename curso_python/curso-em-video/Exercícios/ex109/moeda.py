def metade(n1=0, formato=False):
    resp = n1 / 2
    return resp if formato is False else moeda(resp)


def dobro(n1=0, formato=False):
    r = n1 * 2
    return r if formato is False else moeda(r)


def aumentar(n1=0, taxa=0, formato=False):
    resposta = n1 + (n1 * taxa/100)
    return resposta if formato is False else moeda(resposta)


def diminuir(n1=0, taxa=0, formato=False):
    resp = n1 - (n1 * taxa/100)
    return resp if formato is False else moeda(resp)

def moeda(n1=0, moeda='R$'):
    return f'{moeda}{n1:.2f}'.replace('.', ',')

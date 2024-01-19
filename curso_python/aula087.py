import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=22)

dados = {
    'nome': 'Ariston',
    'sobrenome': 'Silva',
    'idade': '42',
    'cpf': '88736466115'
}

p(dados['cpf'])
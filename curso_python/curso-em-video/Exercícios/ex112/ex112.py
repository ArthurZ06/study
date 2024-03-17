from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiadinheiro(float(input('Digite o preço: R$')))
moeda.resumo(p, 20, 12)

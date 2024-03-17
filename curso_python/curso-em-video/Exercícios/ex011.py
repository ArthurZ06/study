import math

larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('sua parede  tem a dimensão de {} X {} e sua area é de {}m².'.format(larg ,alt , area))
tinta = area / 2
print('para pintar essa parede vc precissará de {}L de tinta'.format(tinta))

distãncia = float(input('Qual é a distância da sua viagem?'))
print('você est[a prestes a começar um viagem de {}Km.'.format(distãncia))

if distãncia <=200:
    preço =distãncia * 0.50
else:
    preço = distãncia * 0.45
print('É o preço da sua passagem será de R${:.2f}'.format(preço))
nome =str(input('Digite seu nome completo:')).upper().lower().split()
print('Muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
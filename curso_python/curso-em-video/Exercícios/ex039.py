from datetime import date

atual = date.today().year
nascimento = int(input('\033[34mEm qual ano você nasceu?\033[m '))
idade = atual - nascimento

if idade < 18:
    print('Quem nasceu em {} tem {} anos em 2023. '.format(nascimento, idade))
    saldo = idade - 18
    print('Ainda falta {} anos para o alistamento '.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em 2023. '.format(nascimento, idade))
    print('Você precissa se alistar IMEDIATAMETE ')
elif idade > 20:
    print('Quem nasceu em {} tem {} anos em 2023. ')
    saldo = saldo = 18 - idade
    print('VocÊ já deveria ter se alistado há mais de {} atrás '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))



n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

soma = n1 + n2
divisao = soma / 3

if divisao < 7.0:
    print(f'A média é {divisao} e infelizmente o aluno está retido :(')
else:
    print(f'A média é {divisao} e aluno está promovido ao próximo ano :)')
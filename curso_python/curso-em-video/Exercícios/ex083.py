pilha = list()
expr = str(input('Dgite a expressão: '))
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len( pilha) == 0:
    print('Sua expressão está válida! ')
else:
    print('Sua expressão está invalida! ')

print('LOJAS AMERICANAS')
valor = float(input('valor das compras:R$ '.strip()))
print('FORMAS DE PAGAMENTO ')
print('[ 1 ] à vista dinheiro/cheque ')
print('[ 2 ] à vista cartão ')
print('[ 3 ] 2x no cartão ')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Sua opçâo: '))

if opção == 1:
    primeiro = (valor - valor * 10 / 100)
    print('O valor inicial é de {} com 10% de desconto ficara {} '.format(valor, primeiro))
elif opção == 2:
    segundo = (valor - valor * 5 / 100)
    print('O valor inicial é de {} com 5% de desconto ficara {} '.format(valor, segundo))
elif opção == 3:
    terceiro = (valor / 2)
    print('A parcela vai ser de 2x de {} '.format(terceiro))
elif opção == 4:
    parcelar = int(input('Quantas vezes no cartão: '))
    quarto = (valor / parcelar)
    quartoo = (valor + valor * 20 / 100)
    print('A parcela vai ser R${:.0f} é o valor final R${}'.format(quarto, quartoo))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO.Tente novamente! ')

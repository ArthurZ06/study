# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Escreve ai marreco: ')
    letras.add(letra.lower())

    if 'cansado' in letras:
        print('Parabéns marreco')
        break

    print(letras)

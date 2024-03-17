sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos.Por favor, informe seu sexo: ')).strip().upper()
print('O sexo {} foi registrado com sucesso'.format(sexo))
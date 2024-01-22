sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo: ')).upper()
    if (sexo != 'F') and (sexo != 'M'):
        print('Digite novamente!\n')

print('Obrigado!!')
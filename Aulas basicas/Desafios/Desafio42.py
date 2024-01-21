n1 = float(input('Digite o comprimento do seguimento 01: '))
n2 = float(input('Digite o comprimento do seguimento 02: '))
n3 = float(input('Digite o comprimento do seguimento 03: '))

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n2 + n3 > n1):
    if n1 == n2 and n2 == n3:
        tipo = 'equilatero'

    elif (n1 != n2) and (n1 != n3) and (n2 != n3):
        tipo = 'escaleno'

    else:
        tipo = 'isosceles'

    print(f'Os segmentos formam um triangulo do tipo: {tipo}')

else:
    print('Segmentos nao formam um triangulo')
r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de uma reta: '))
r3 = float(input('Digite o comprimento de uma reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('As tres retas podem formar um triangulo! :)')
else:
    print('As tres retas nao podem formar um triangulo! :(')

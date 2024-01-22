numero = int(input('Digite um numero: '))
cont = numero-1
fac = numero

while cont != 0:
    fac *= cont
    cont -= 1

print(f'O fatorial de {numero} eh {fac}')
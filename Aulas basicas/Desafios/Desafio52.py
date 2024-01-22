num = int(input('Digite um numero: '))

if num < 0:
    num *= -1

cont = 0
for i in range(1, num+1):
    if num % i == 0:
        cont += 1

if cont == 2:
    print('Eh primo')
else:
    print('Nao eh primo')
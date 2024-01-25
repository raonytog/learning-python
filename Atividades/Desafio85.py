numeros = list()
pares = list()
impares = list()

for i in range(0, 7):
    num = int(input(f'Digite um numero #{i+1}: '))
    print('-=-'*10)

    if num % 2 == 0:
        pares.append(num)

    else:
        impares.append(num)

pares.sort()
impares.sort()

numeros.append(pares)
numeros.append(impares)

print(f'Os numeros impares: {numeros[1]}')
print(f'Os numeros pares: {numeros[0]}')


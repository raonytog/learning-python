pares, impares, val = [], [], []
i = -1
while True:
    i += 1
    val.append(int(input('Digite um numero: ')))
    if val[i] % 2 == 0:
        pares.append(val[i])

    else:
        impares.append(val[i])

    opcao = str(input('Deseja continuar? [S/N] ')).upper()
    if opcao == 'N':
        break

print(f'Lista de numeros impares: {impares}')
print(f'Lista de numeros pares: {pares}')

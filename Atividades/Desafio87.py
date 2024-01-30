# matriz + condicoes

matrix = list()
sumPares = 0
sumTerceiraColuna = 0
maiorValorSegundaLinha = -999999

for i in range(0, 3):
    print('-=-'*10)
    rows = list()
    for j in range(0, 3):
        num = float(input(f'Digite um numero [{i}][{j}]: '))
        rows.append(num)

    matrix.append(rows)

for i in range(0, 3):
    for j in range(0, 3):
        # se for par
        if matrix[i][j] % 2 == 0:
            sumPares += matrix[i][j]

        # se for a terceira coluna
        if j == 2:
            sumTerceiraColuna += matrix[i][j]

        # maior valor da segunha linha
        if i == 1:
            if matrix[i][j] > maiorValorSegundaLinha:
                maiorValorSegundaLinha = matrix[i][j]

for i in range(0, 3):
    print()
    for j in range(0, 3):
        print(f'[{matrix[i][j]:.2f}] ', end='')

print(f'\n\nA soma dos pares: {sumPares}')
print(f'A soma da terceira coluna: {sumTerceiraColuna}')
print(f'O maior valor da segunda linha: {maiorValorSegundaLinha}')
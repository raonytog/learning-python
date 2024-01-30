# matriz

matrix = list()

for i in range(0, 3):
    rows = list()
    for j in range(0, 3):
        num = float(input(f'Digite um numero [{i}][{j}]: '))
        rows.append(num)

    matrix.append(rows)

for i in range(0, 3):
    print()
    for j in range(0, 3):
        print(f'[{matrix[i][j]:.2f}] ', end='')






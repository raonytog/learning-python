# Gerador de jogadas da mega sena

from random import randint

matriz = list()
numLinhas = 0
while numLinhas <= 0:
    print('-' * 50)
    numLinhas = int(input('Quer sortear quantos jogos? '))
    if numLinhas <= 0:
        print('-'*10)
        print('Erro, digite um numero maior que 0!')
        print('-' * 10)

for i in range(0, numLinhas):
    rows = list()
    for j in range(0, 6):
        rows.append(randint(1, 60))

    rows.sort()
    matriz.append(rows)

for i in range(0, numLinhas):
    print(f'Jogo #{i+1}: ', end='')
    print(matriz[i])




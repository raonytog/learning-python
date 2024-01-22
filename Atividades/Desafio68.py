from random import randint

vitorias = 0
while True:
    jogada = str(input('Digite se escolhe par ou impar [P/I]: ')).upper()
    jogador = int(input('Digite um numero entre 1 e 10: '))
    computador = randint(1, 10)
    print(f'A jogada do computador foi: {computador}')
    sum = jogador + computador

    if sum % 2 == 0:
        if jogada == 'P':
            vitorias += 1
            print('Vitoria do jogador!')

        else:
            print('Derrota do jogador!')
            break

    else:
        if jogada == 'I':
            vitorias += 1
            print('Vitoria do jogador!')

        else:
            print('Derrota do jogador!')
            break

print(f'O jogador teve uma sequencia de {vitorias} vitorias')

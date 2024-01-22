from random import randint

# 0 - pedra
# 1 - papel
# 2 - tesoura

jogadaComputador = randint(0, 2)
jogadaPessoa = str(input('Digite uma jogada para o jokenpo: ')).lower().strip()

if jogadaComputador == 0:
    print(f'pedra x {jogadaPessoa}')

elif jogadaComputador == 1:
    print(f'papel x {jogadaPessoa}')

else:
    print(f'tesoura x {jogadaPessoa}')

if jogadaPessoa == 'pedra':
    if jogadaComputador == 0:
        print('Empate')

    elif jogadaComputador == 1:
        print('Vitoria do computador!')

    else:
        print('Vitoria do jogador!')

if jogadaPessoa == 'papel':
    if jogadaComputador == 0:
        print('Vitoria do jogador!')

    elif jogadaComputador == 1:
        print('Empate')

    else:
        print('Vitoria do computador!')

if jogadaPessoa == 'tesoura':
    if jogadaComputador == 0:
        print('Vitoria do computador!')

    elif jogadaComputador == 1:
        print('Vitoria do jogador!')

    else:
        print('Empate')

import random

numSorteado = random.randint(0, 5)
num = int(input('Adivinhe o numero escolhido pelo computador: '))
if num == numSorteado:
    print('Parabens!!')
else:
    print('Mais sorte na proxima :(')

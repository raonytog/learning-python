from random import randint

numeroSorteado = randint(0, 10)
num = -1
cont = 0
while num != numeroSorteado:
    if cont > 0:
        print('Tente novamente!\n')
    num = int(input('Tente adivinhar o numero aleatorio (0 a 10) da maquina: '))
    cont += 1

print(f'Foram necessarias {cont} tentativas para adivinhar o numero {numeroSorteado}')

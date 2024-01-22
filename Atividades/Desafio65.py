media, cont = 0, 0
maior = -999999
menor = 999999

exit = 0
while True:
    num = int(input('Digite um numero: '))
    media += num
    cont += 1

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    exit = int(input('Deseja continuar? '))
    if exit == 1:
        continue
    else:
        break


print(f'O maior, o menor e a media, respectivamente: {maior}, {menor} e {media/cont:.2f}')

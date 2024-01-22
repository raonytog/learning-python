num, sum, cont = 0, 0, 0
while num != 999:
    cont += 1
    num = int(input(f'Digite um numero ({cont}): '))
    sum += num

print(f'Qtd de numeros digitados ate 999: {cont}')
print(f'Soma dos numeros digitados: {sum}')
sum = 0
for i in range(0, 6):
    num = float(input('Digite um numero: '))
    if num % 2 == 0:
        sum += num

print(f'A soma dos numeros pares eh: {sum}')
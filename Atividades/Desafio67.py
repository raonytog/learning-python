while True:
    num = float(input('Digite um numero: '))
    if num < 0:
        break

    else:
        for i in range(0, 10):
            print(f'{num} x {i+1} = {num * (i+1)}')

print('Voce digitou um numero negativo')
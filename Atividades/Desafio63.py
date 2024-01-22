cont = 0
fib1 = 0
fib2 = 1

num = int(input('Digite quantos termos deseja ver na sequencia de fibonacci: '))

while cont != num:
    if cont == 0:
        print(f'1 - {fib1}')

    elif cont == 1:
        print(f'2 - {fib2}')

    else:
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
        print(f'{cont+1} - {sum}')

    cont += 1
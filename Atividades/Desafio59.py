opcao = 0
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

while opcao != 5:
    print('-'*30)
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR DO PROGRAMA')
    print('-' * 30)
    opcao = int(input('Digite a opcao desejada: '))

    if opcao == 1:
        print(f'{n1:.2f} + {n2:.2f} = {n1+n2:.2f}')

    elif opcao == 2:
        print(f'{n1:.2f} + {n2:.2f} = {n1*n2:.2f}')

    elif opcao == 3:
        if n1 > n2:
            print(f'o numero {n1:.2f} eh maior que {n2:.2f}')

        else:
            print(f'o numero {n2:.2f} eh maior que {n1:.2f}')

    elif opcao == 4:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite um numero: '))

    else:
        break


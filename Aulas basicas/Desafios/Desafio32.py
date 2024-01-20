ano = int(input('Digite um ano: '))

if ano/4 and ano/100 and ano%400 == 0:
    print(f'{ano} eh um ano bissexto!')
else:
    print(f'{ano} nao eh um ano bissexto!')
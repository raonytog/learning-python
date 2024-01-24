
expressao = str(input('Digite a expressao: '))

oppend = expressao.count('(')
closed = expressao.count(')')

if oppend == closed:
    print('Eh uma expressao valida!')
else:
    print('Nao eh uma expressao valida. :(')

palavras = ('teste', 'raony', 'python')

for i in range(0, 3):
    contA = palavras[i].count('a')
    contE = palavras[i].count('e')
    contI = palavras[i].count('i')
    contO = palavras[i].count('o')
    contU = palavras[i].count('u')
    print(f'{palavras[i]} tem as vogais: ',end='')
    if contA > 0:
        print('a ', end='')

    if contE > 0:
        print('e ', end='')

    if contI > 0:
        print('i ', end='')

    if contO > 0:
        print('o ', end='')

    if contU > 0:
        print('u ', end='')

    print('')
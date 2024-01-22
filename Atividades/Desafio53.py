frase = str(input('Digite sua frase: ')).replace(' ', '')
fraseInv = frase[::-1]

if frase == fraseInv:
    print('Eh palindromo')

else:
    print('Nao eh palindromo')
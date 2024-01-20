frase = 'Curso em video python e amor'
# [start:stop:step]

print(f"{frase[9:13]}") #output: vide
print(f"{frase[9:14]}") #output: video
print(f"{frase[9:21]}") #output: video python

print(f"{frase[9:21:2]}") #output: vdopto (pula de 2 em 2)
print(f"{frase[:5]}") #output: Curso (eh o ponto de parada, de 0 ate o numero)
print(f"{frase[15:]}") #output: python (eh o ponto de inicio ate o final)
print(f"{frase[9::3]}") #output: veph (comeca em 9 e vai ate o final, pulando 3 char)

print(f"tamanho da frase eh {len(frase)}")

print(f"{frase[:13]}") #output: video python
qtdDeO = frase.count('o',0,13)
print(f"qtd de 'o' na tela: {qtdDeO}")

indx = frase.find('video')
print(f"'video' inicia no indice: {indx}")

indx = frase.find('teste')
print(f"'teste' inicia no indice: {indx}")

if ('Curso' in frase):
    print('sim')

sec = frase.replace('python', 'Avaraquedabra')
print(f"a frase ficou:\t {sec}")

upperStr = sec.upper()
print(f'{upperStr}')

lowerStr = sec.lower()
print(f'{lowerStr}')

captalizeStr = sec.capitalize()
print(f'{captalizeStr}')

tittleStr = sec.title()
print(f'{tittleStr}')

newStr = '   Aprenda Python  '
print(f'Nova frase: {newStr}\nTamanho: {len(newStr)}')

strippedStr = newStr.strip()
print(f'Stripped string: {strippedStr}; e o tamanho: {len(strippedStr)}')

rStrippedStr = newStr.rstrip()
print(f'R stripped string: {rStrippedStr}; e o tamanho: {len(rStrippedStr)}')

lStrippedStr = newStr.lstrip()
print(f'L stripped string: {lStrippedStr}; e o tamanho: {len(lStrippedStr)}')


lista = frase.split()
print(f'{lista}')
nova = '-'.join(frase)
print(f'{nova}')



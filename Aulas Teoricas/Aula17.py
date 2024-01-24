# listas
print('#'*50)
lanche = ['hamburguer', 'pizza']
lanche.append('sorvete') # add e realoca um elemento ao vetor na ultima posicao
print('APPEND:')
print(lanche)
print('#'*50)

lanche.insert(0, 'natchos') # realoca e add um elemento ao vetor na posicao x
print('INSERT:')
print(lanche)
print('#'*50)

del lanche[0] # elimita o indice (alternativa ao pop)
lanche.pop(1) # passa-se como parametro o indice a eliminar
lanche.remove('sorvete') # passa-se o conteudo
print('DEL, POP E REMOVE:')
print(lanche)

print('REMOVE COM IF')
lanche.append('batatas')
if 'batatas' in lanche:
    lanche.remove('hamburguer')
    print(lanche)

print('#'*50)
print('COM NUMEROS - ORDENADOS: ')
valores = list(range(4, 11))
print(valores)

print('#'*50)
print('COM NUMEROS - DESORDENADOS, POSTERIORMENTE ORDENADOS: ')
val = [1, 0, 90, 32, -7]
print(val) # desordenado

val.sort()
print(val) # crescente

val.sort(reverse=True)
print(val) # decrescente


# tuplas

# () tupla
# [] lista
# {} dicionario

lanche = sorted(('hamburguer', 'suco', 'pizza', 'pudim', 'batata-frita'))
print(lanche)

print('*'*30)
for i, comida in enumerate(lanche):
    print(f'{i+1} - {comida}')
print('Comida demais...')
print('*'*30)

vA = (1, 2, 3, 1, 2)
vB = (9, 8, 7, 1, 0)
vC = vA + vB
print(sorted(vC)[::-1])
print(vC.count(1))
print(vC.index(9))

del(comida)



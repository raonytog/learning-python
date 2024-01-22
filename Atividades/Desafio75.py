n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))

vet = (n1, n2, n3, n4)
cont9 = 0
pares = 0
for i in vet:
    if i == 9:
        cont9 += 1

print('-*-'*10)
print(f'O valor 9 apareceu {cont9} vezes')
print(f'A posicao em que apareceu o valor 3 pela primeira vez foi a {vet.index(3)}')
print(f'Os numeros pares foram os:')
for i in vet:
    if i % 2 == 0:
        print(f'\t{i} ')
print('-*-'*10)


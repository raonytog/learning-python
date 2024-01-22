from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)

maior = -11
menor = 11
vet = (n1, n2, n3, n4, n5)
print('Listagem dos numeros: ')
print(vet)

for i in vet:
    if i < menor:
        menor = i

    if i > maior:
        maior = i

print(f'O maior e o menor numero da listagem, respectivamente: {maior} e {menor}')
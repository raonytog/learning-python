n1 = int(input('Digite um nunero: '))
n2 = int(input('Digite um nunero: '))
n3 = int(input('Digite um nunero: '))
numeros = [n1, n2, n3]

maior = 0
menor = 999999

for i in range(0, 3):
    if numeros[i] > maior:
        maior = numeros[i]

    if numeros[i] < menor:
        menor = numeros[i]

print(f'O maior numero eh: {maior}\nO menor numero eh: {menor}')




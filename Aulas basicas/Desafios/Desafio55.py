menor = 999
maior = 0

for i in range(0, 5):
    peso = float(input(f'Digite o peso da pessoa {i+1}: '))
    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f'O maior peso e o menor sao, respectivamente: {maior:.2f} kg e {menor:.2f} kg')
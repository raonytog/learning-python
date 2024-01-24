valores = []
menor = 999999
maior = -999999

for i in range(0, 5):
    valores.append(int(input('Digite um numero: ')))
    if valores[i] > maior:
        maior = valores[i]

    if valores[i] < menor:
        menor = valores[i]

print(f'O maior numero e sua posicao eh, respectivamente: {maior} e {valores.index(maior)}')
print(f'O menor numero e sua posicao eh, respectivamente: {menor} e {valores.index(menor)}')

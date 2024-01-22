frase = str(input('Digite uma frase: ')).strip()
size = len(frase)

qttA = frase.count('A')
print(f"A letra 'A' aparece {qttA} vezes")

idx = frase.find('A')
print(f"A letra 'A' aparece pela primeira vez no indice: {idx}")

idx2 = frase[::-1].find('A')
print(f"A letra 'A' aparece pela ultima vez no indice: {size - idx2 - 1}")



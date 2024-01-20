# aula de modulos

import random
import math # importou todas as funcoes
import emoji
# from math import sqrt, ceil # so importou sqrt e ceil


num = random.randrange(0, 999, 2)
print("Biblioteca matematica: ")
print(f"{num}")
raiz = math.sqrt(num) # com import math
# raiz = sqrt(num) # com import math


arredondado = math.ceil(num)
# arredondado = ceil(num)

print(f"a raiz quadrada de {num} eh {raiz}")
print(f"o num {num} arredondado fica como: {arredondado}\n")

print("Emojis agora: ")
print(emoji.emojize("Python eh bem :grinning_face:"))
print(emoji.emojize("Ola, :globe_showing_Americas:!"))
# Truncar um numero, ex: in[9.123] -> out[9]

from math import trunc
num = float(input("Digite um numero flutuante: "))
truncado = trunc(num)
print(f"o numero truncado eh: {truncado}")  
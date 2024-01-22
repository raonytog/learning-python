# Calcular a hipotenusa, dado os dois catetos

from math import sqrt

num1 = float(input("Digite o cateto oposto: "))
num2 = float(input("Digite o cateto adjacente: "))

print(f"A hipotenusa eh: {sqrt(num1**2 + num2**2)}")
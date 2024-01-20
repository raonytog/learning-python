numeral = input("Digite um numero de 0 a 9999: ")
size = len(numeral)

print(f'unidade: {numeral[size-1]}')
print(f'dezena: {numeral[size-2]}')
print(f'centena: {numeral[size-3]}')
print(f'milhar: {numeral[size-4]}')
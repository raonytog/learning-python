# por string
numeral = input("Digite um numero de 0 a 9999: ")
size = len(numeral)

print(f'unidade: {numeral[size-1]}')
print(f'dezena: {numeral[size-2]}')
print(f'centena: {numeral[size-3]}')
print(f'milhar: {numeral[size-4]}')

# por matematica (mal feita)
numeral = int(input("Digite um numero de 0 a 9999: "))
print(f'unidade: {(numeral%10)}')
print(f'dezena: {((numeral//10)%100)%10}')
print(f'centena: {(numeral//100)%10}')
print(f'milhar: {numeral//1000}')
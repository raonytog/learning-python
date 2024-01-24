val = []

while True:
    num = int(input('Digite um numero: '))
    if val.count(num) == 0:
        val.append(num)
    print('Deseja adicionar mais um numero? [S/N]')

    opcao = str(input('')).upper()
    if opcao == 'N':
        break

val.sort()
print(val)

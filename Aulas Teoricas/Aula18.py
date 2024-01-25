# listas, parte 2

galera = list()

data = list()
for c in range(0, 3):
    data.append(str(input('Digite o nome: ')))
    data.append(int(input('Digite a idade: ')))
    # caso nao use [:], sera passado o endereco da variavel
    # e os valores podem ser alterados posteriormente
    galera.append(data[:])
    data.clear()

print(galera)
totalMaior = 0
totalMenor = 0

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} eh maior de idade')
        totalMaior += 1

    else:
        totalMenor += 1
        print(f'{p[0]} eh menor de idade')

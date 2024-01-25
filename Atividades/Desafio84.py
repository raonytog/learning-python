
lista = list()
pessoas = list()

maisPesado = -999999
menosPesado = 999999
qtdCadastrados = 0

while True:
    print('-=-'*10)
    pessoas.append(str(input('Nome: ')).title())
    pessoas.append(float(input('Peso: ')))
    lista.append(pessoas[:])
    pessoas.clear()

    qtdCadastrados += 1
    opcao = str(input('Deseja adicionar mais pessoas? [S/N] ')).upper()
    if 'N' in opcao:
        break

print(lista)
print(f'Na lista, foram cadastradas {qtdCadastrados} pessoas.')

# ordena com base no peso (menor pro maior)
for j in range(0, len(lista)):
    for k in range(j+1, len(lista)):
        if lista[j][1] > lista[k][1]:
            temp = lista[j]
            lista[j] = lista[k]
            lista[k] = temp

# encontra o maior e menor peso
for i in range(0, len(lista)):
    if lista[i][1] > maisPesado:
        maisPesado = lista[i][1]

    if lista[i][1] < menosPesado:
        menosPesado = lista[i][1]

print(f'A lista na ordem lida, com {qtdCadastrados} pessoas cadastradas: {lista}')
print('A lista em ordem do mais pesado para o menos pesado:')
for m in range(len(lista)-1, -1, -1):
    print(f'{lista[m][0] }', end='')

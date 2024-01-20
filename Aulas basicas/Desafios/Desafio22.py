name = input("Digite o nome completo: ")
sizeWOWhiteSpace = len(name) - name.count(' ')

lista = name.split()
firstNameSize = len(lista[0]) # tamanho do primeiro nome
print(f'O nome em maiusculo: {name.upper()}')
print(f'O nome em minusculo: {name.lower()}')
print(f'Tamanho do nome, sem espacos: {sizeWOWhiteSpace}')
print(f'Tamanho do primeiro nome: {firstNameSize}')


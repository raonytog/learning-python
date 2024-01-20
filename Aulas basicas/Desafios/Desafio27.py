fullName = str(input('Digite o nome completo: ')).strip()
list = fullName.split()
listLenght = len(list)

print(f'O primeiro nome eh: {list[0]}')
print(f'O ultimo nome eh: {list[listLenght-1]}')
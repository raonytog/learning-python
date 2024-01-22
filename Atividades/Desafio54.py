cont = 0
for i in range (0, 7):
    anoNascimento = int(input(f'Digite o ano de nascimento da pessoa #{i+1}: '))
    if 2024 - anoNascimento >= 18:
        cont += 1

print(f'{cont} ja atingiram a maioridade')


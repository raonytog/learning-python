nomeHomemMaisVelho = ''
idadeHomemMaisVelho = 0

mediaIdades = 0

qtdMulheresMenoridade = 0

for i in range (0, 4):
    print('-'*30)
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: '))

    if sexo == 'masculino':
        if idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome

    else:
        if idade < 18:
            qtdMulheresMenoridade += 1

    mediaIdades += idade

print(f'A media das idades eh: {mediaIdades}')
print(f'O nome do homem mais velho eh: {nomeHomemMaisVelho}')
print(f'A quantidade de mulheres na menoridade: {qtdMulheresMenoridade}')
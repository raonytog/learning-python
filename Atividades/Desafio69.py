maioridade = 0
homensCadastrados = 0
mulheresMenoridade = 0
sexo = ''

while True:
    idade = int(input('Digite a idade: '))

    while sexo != 'masculino' and sexo != 'feminino':
        sexo = str(input('Digite o sexo: '))

    if idade > 18:
        maioridade += 1

    if sexo == 'masculino':
        homensCadastrados += 1

    if sexo == 'feminino' and idade < 18:
        mulheresMenoridade += 1

    print('Deseja ler mais uma pessoa? [S/N]')
    opcao = str(input()).upper()
    if opcao == 'N':
        break

print(f'Quantiade de pessoas na maioridade: {maioridade}')
print(f'Quantidade de homens cadastrados: {homensCadastrados}')
print(f'Quantidade de mulheres na menoridade: {mulheresMenoridade}')
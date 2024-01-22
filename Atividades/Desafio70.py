precoTotal = 0
qtdProdutosAcima1000 = 0
produtoMaisBarato = ''
menorPreco = 999999

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))

    if preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = nome

    if preco > 1000:
        qtdProdutosAcima1000 += 1

    precoTotal += preco
    print('Deseja inserir mais produtos? [S/N]')
    opcao = str(input('')).upper()
    if opcao == 'N':
        break

print(f'Preco total: R${precoTotal:.2f}')
print(f'Quantidade de produtos acima de R$1000,00: {qtdProdutosAcima1000}')
print(f'Nome do produto mais barato: {produtoMaisBarato}')


nome1, preco1 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome2, preco2 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome3, preco3 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome4, preco4 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome5, preco5 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome6, preco6 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome7, preco7 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome8, preco8 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))
nome9, preco9 = str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: '))

listagem = (nome1, preco1, nome2, preco2, nome3, preco3,
            nome4, preco4, nome5, preco5, nome6, preco6,
            nome7, preco7, nome8, preco8, nome9, preco9)

print('-=-'*30)
print('LISTAGEM DE PRECOS DA VENDA')
print('-=-'*30)
for i in range(0, 18, 2):
    print(f'{listagem[i]}', end='')
    print('.'*(30-len(listagem[i])), end='')
    print(f'R$ {listagem[i+1]:.2f}')
print('#'*30)


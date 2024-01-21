precoProduto = float(input('Digite o preco do produto: '))
formaPagamento = str(input('Digite a forma de pagamento: '))

if (formaPagamento == 'a vista dinheiro') or (formaPagamento == 'a vista cheque'):
    print(f'preco a ser pago, com 10% de desconto: R${ (precoProduto * (100 - 10)) / 100:.2f}')

elif formaPagamento == 'a vista no cartao':
    print(f'preco a ser pago, com 5% de desconto: R${ (precoProduto * (100 - 5) ) / 100:.2f}')

elif formaPagamento == '2x no cartao':
    print(f'preco a ser pago, com 5% de desconto: R${precoProduto:.2f}')

else:
    print(f'preco a ser pago, com 20% de juros: R${ (precoProduto * (100 + 20) ) / 100:.2f}')

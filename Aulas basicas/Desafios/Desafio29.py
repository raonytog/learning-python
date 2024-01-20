velocidade = float(input('Digite a velocidade atingida pelo veiculo: '))
if velocidade > 80:
    print(f'Voce ultrapassou o limite da via e devera pagar: R${(velocidade-80)*7:.2f}')
else:
    print('Continue assim :)')

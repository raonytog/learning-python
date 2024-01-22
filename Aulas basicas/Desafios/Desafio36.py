valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario do comprador? '))
anos = int(input('Em quantos anos vai querer pagar? '))

custoPrestacoes = valorCasa / (anos * 12)

if custoPrestacoes <= ((salario * 30)/100):
    print(f'A compra foi autorizada e o comprador devera pagar R${custoPrestacoes:.2f} por mes durante {anos}', end='')
    print(' Boa sorte!')
else:
    print(f'Compra nao autorizada, dando R${custoPrestacoes:.2f}, excedendo os 30% do salario! :(')

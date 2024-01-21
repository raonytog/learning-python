valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario do comprador? '))
anos = float(input('Em quantos anos vai querer pagar? '))

custoPrestacoes = valorCasa/anos



if custoPrestacoes <= ((salario * 30)/100):
    print(f'A compra foi autorizada e o comprador devera pagar R${custoPrestacoes:.2f} por mes durante {anos}')
else:
    print('Compra nao autorizada! :(')

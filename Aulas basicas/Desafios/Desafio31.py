distancia = float(input('Digite a quilometragem percorrida na viagem: '))

if distancia <= 200:
    print(f'Voce devera pagar R${distancia*0.5:.2f}')
else:
    print(f'Voce devera pagar R${distancia * 0.45:.2f}')
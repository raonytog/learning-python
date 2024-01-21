peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/(altura**2)

if imc < 18.5:
    print(f'Abaixo do peso {imc}')

elif imc >= 18.5 and imc < 25:
    print(f'Peso ideal {imc}')

elif imc >= 25 and imc < 30:
    print(f'Sobrepeso {imc}')

elif imc >= 30 and imc < 40:
    print(f'Obesidade {imc}')

else:
    print(f'Obesidade morbida {imc}')
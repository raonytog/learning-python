salario = float(input('Digite o seu salario: '))
newSalario = 0

if salario <= 1250:
    newSalario = (salario * (100+15))/100
    print(f'Este eh o salario com o aumento de 15%: {newSalario:.2f}')
else:
    newSalario = (salario * (100+10))/100
    print(f'Este eh o salario com o aumento de 10%: {newSalario:.2f}')


salarioBase = float(input("Digite o salario base: "))
porcentagemDeAumento = int(input("Digite a porcentagem de aumento: "))

salarioComAumento = (salarioBase * (100 + porcentagemDeAumento))/100
print(f"O salario de R${salarioBase:.2f} com aumento de {porcentagemDeAumento}% passou a ser R${salarioComAumento:.2f}")
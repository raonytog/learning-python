precoReal = float(input("Qual o preco do produto? "))
desconto = int(input("Qual o desconto sera dado ao produto? "))

precoComDesconto = (precoReal * (100 - desconto))/100
print(f"O produto com o preco de R${precoReal:.2f} com desconto de {desconto}% ficou com o custo de R${precoComDesconto:.2f}")
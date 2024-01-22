largura = int(input("Qual a largura da parede? "))
altura = int(input("Qual a altura da parede? "))

areaTotal = largura * altura
qtdTintaNecessaria = areaTotal/2

print(f"Sera necessario {qtdTintaNecessaria}L de tinta para pintar a parede com area {areaTotal}m²")
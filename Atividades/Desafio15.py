dias = int(input("Digite quantos dias foram usados: "))
quilometros = float(input("Digite os kilometros percorridos: "))

totalPorDias = dias * 60
totalPorKm = quilometros * 0.15

totalEmReais = totalPorDias + totalPorKm
print(f"Preco a pagar: {totalEmReais:.2f}")
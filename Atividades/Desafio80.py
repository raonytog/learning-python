val = []

for i in range(0, 5):
    num = int(input('Digite um numero: '))
    val.append(num)

    if len(val) >= 2:
        for j in range(0, len(val)):
            for k in range(0, len(val)):
                if val[j] < val[k]:
                    temp = val[j]
                    val[j] = val[k]
                    val[k] = temp

print(val)

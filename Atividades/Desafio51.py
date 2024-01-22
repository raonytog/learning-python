t1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razao da PA: '))

sum = t1
print(f'1 - {t1}')
for i in range(2, 11):
    sum += r
    print(f'{i} - {sum}')
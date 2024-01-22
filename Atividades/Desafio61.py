t1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razao da PA: '))
cont = 2
nt = t1

print(f'1 - {t1}')
while cont < 11:
    nt += r
    print(f'{cont} - {nt}')
    cont += 1

c50, c20, c10, c1 = 0, 0, 0, 0
r50, r20, r10, r1 = 0, 0, 0, 0
t50, t20, t10, t1 = 0, 0, 0, 0
sum = 0

while True:
    desejado = int(input('Digite quantas cedulas deseja sacar: '))
    c50 = desejado // 50
    r50 = desejado % 50
    t50 += c50

    c20 = r50 // 20
    r20 = r50 % 20
    t20 += c20

    c10 = r20 // 10
    r10 = r20 % 10
    t10 += c10

    c1 = r10 // 1
    t1 += c1

    print('Quantidade de celulas totais:')
    print(f'\t 50 - {c50}')
    print(f'\t 20 - {c20}')
    print(f'\t 10 - {c10}')
    print(f'\t 1  - {c1}')
    print('Deseja sacar mais dinheiro? [S/N]')
    opcao = str(input('')).upper()
    if opcao == 'N':
        break

print('Quantidade de celulas totais:')
print(f'\t 50 - {t50}')
print(f'\t 20 - {t20}')
print(f'\t 10 - {t10}')
print(f'\t 1  - {t1}')
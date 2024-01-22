t1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razao da PA: '))
cont = 0
nt = t1
opcao = 0
sair = 0

while True:
    sair = 0
    print(f'{cont + 1} - {nt}')
    nt += r
    cont += 1

    if cont % 10 == 0:
        opcao = str(input('Deseja mostrar mais termos? '))
        if opcao == 0:
            sair = 1

    if sair:
        break
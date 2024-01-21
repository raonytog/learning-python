n1 = float(input('Digite a nota #1: '))
n2 = float(input('Digite a nota #2: '))

media = (n1 + n2)/2
if media < 5:
    print('REPROVADO!')

elif media >= 5 and media <= 6.9:
    print('RECUPERACAO!')

else:
    print('APROVADO, PARABENS!!')
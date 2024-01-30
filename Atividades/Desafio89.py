
matriz = list()
numAlunos = 0

while numAlunos <= 0:
    numAlunos = int(input('Digite quantos alunos serao lidos: '))

for i in range(0, numAlunos):
    alunos = list()
    print('-=-' * 10)
    nome = str(input('Digite o nome do aluno: '))
    alunos.append(nome)

    n1 = int(input('Nota #1: '))
    alunos.append(n1)

    n2 = int(input('Nota #2: '))
    alunos.append(n2)

    matriz.append(alunos)

print('-=-'*10)
print('BOLETIM')
print('-=-'*10)
for i in range(0, numAlunos):
    print(matriz[i][0], end='')
    print('.'*(20 - len(matriz[i][0])), end='')
    print(matriz[i][1], matriz[i][2], (matriz[i][1] + matriz[i][2])//2)
print('-=-'*10)

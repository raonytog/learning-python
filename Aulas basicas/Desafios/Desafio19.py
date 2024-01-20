# sorteia um aluno e printa o nome dele

import random

aluno1 = str(input("Digite o nome do aluno: "))
aluno2 = str(input("Digite o nome do aluno: "))
aluno3 = str(input("Digite o nome do aluno: "))
aluno4 = str(input("Digite o nome do aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.sample(lista, 1)
print(f"O aluno sorteado foi o: {sorteado}")
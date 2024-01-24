
val = []
while True:
    val.append(int(input('Digite um numero: ')))
    opcao = str(input('Deseja continuar? [S/N] ')).upper()
    if opcao == 'N':
        break

print(f'Foram digitados {len(val)} numeros.')
val.sort(reverse=True)
print(val)

if val.count(5) > 0:
    print(f'Foi achado o numero 5 na posicao {val.index(5)}.')
else:
    print('O valor 5 nao foi encontrado na lista.')

anoNascimento = int(input('Digite o ano de nascimento: '))
idade = 2024 - anoNascimento

if idade > 18: #ja deveria se alistar
    idadeOverflow = idade - 18
    print(f'Ja passaram {idadeOverflow} anos, ta na hora de se alistar!')

elif idade == 18:
    print(f'Voce tem {idade} anos, esta na hora de se alistar')

else:
    idadeUnderflow = (idade - 18)*-1
    print(f'Ainda faltam {idadeUnderflow} anos para se alistar')

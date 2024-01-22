anoDeNascimento = int(input('Digite seu ano de nascimento: '))
idade = 2024 - anoDeNascimento

print('O atleta esta na categoria:')
if idade < 9:
    print('\tmirim')

elif idade < 14:
    print('\tinfantil')

elif idade < 19:
    print('\tjunior')

elif idade < 20:
    print('\tsenior')

else:
    print('\tmaster')
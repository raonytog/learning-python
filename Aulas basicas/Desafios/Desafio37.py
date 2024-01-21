numero = int(input('Digite um numero: '))

print("""-------------------------------\n\t1 - Binario\n\t2 - Octal\n\t3 - Hexadecimal\nDigite a base de conversao:""")
base = str(input(''))

print(f'O numero {numero} convertido da base {base} convertido eh igual a:')
if base == 'binario':
    binario = bin(numero)
    print(f'{binario}')

elif base == 'hexadecimal':
    hexadecimal = hex(numero)
    print(f'{hexadecimal}')

else:
    octal = oct(numero)
    print(f'{octal}')

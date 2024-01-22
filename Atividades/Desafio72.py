numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = -1
while num < 0 or num > 20:
    num = int(input('Digite um numero de 0 a 20 para ver o extenso dele: '))
print(numeros[num])
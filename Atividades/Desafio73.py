times = ('palmeiras', 'gremio', 'atletico', 'flamengo', 'botafogo', 'bragantino',
         'fluminence', 'athletio-pr', 'internacional', 'fortaleza', 'sao paulo',
         'cuiaba', 'corinthians', 'cruzeiro', 'vasco', 'bahia', 'santos', 'goias',
         'curitiba', 'america-mg')

print('Os cinco primeiros colocados sao:')
print(f'\t{times[0:5]}')

print('Os ultimos quatro colocados sao:')
print(f'\t{times[20:15:-1]}')

print('Os times em ordem alfabetica:')
print(f'\t{sorted(times)}')

print('Colocacao do time chapecoence: ')
print(times.index('chapecoence'))



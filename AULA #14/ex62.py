"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

r = int(input('Digite a razão da P.A: '))
primeiro = int(input('Digite o primeiro termo: '))

decimo = primeiro + (10 - 1) * r

while primeiro <= decimo:
    print(f'{primeiro}', end='')
    print(f', ' if primeiro < decimo else '', end='')
    primeiro += r

termos = 1
total = 0

while termos != 0:
    termos = int(input('\nQuantos termos a mais deseja ver? '))
    pos = primeiro + (termos - 1) * r
    total += termos
    while primeiro <= pos:
        print(f'{primeiro}', end='')
        print(f', ' if primeiro < pos else '', end='')
        primeiro += r

print(f'\nProgressão finalizada com {total} termos mostrados')

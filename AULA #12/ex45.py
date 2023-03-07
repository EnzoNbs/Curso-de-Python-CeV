"""
Crie um programa que faça o computador jogar Jokenpô com você
"""

from random import randint
from time import sleep


lances = ['Pedra', 'Papel', 'Tesoura']
cpu = randint(0, 2)
player = int(input('Jogadas\n'
                   '[ 0 ] para PEDRA\n'
                   '[ 1 ] para PAPEL\n'
                   '[ 2 ] para TESOURA\n'
                   'Escolha uma jogada: '))

print(f'\n{"JO":^11}')
sleep(1)
print(f'{"KEN":^12}')
sleep(0.8)
print(f'{"PÔ!":^12}')
sleep(0.3)

if player > 2:
    print('\n\033[34mVocê fez uma jogada errada!')
    exit()

print(f'\n Computador jogou {lances[cpu]}\n Você jogou {lances[player]}')
sleep(1)

if player == cpu:
    print('\033[34m Empate!')
elif cpu == 0 and player == 1:
    print('\033[32m Você venceu!')
elif cpu == 0 and player == 2:
    print('\033[31m Computador venceu!')
elif cpu == 1 and player == 0:
    print('\033[31m Computador venceu!')
elif cpu == 1 and player == 2:
    print('\033[32m Você venceu!')
elif cpu == 2 and player == 0:
    print('\033[32m Você venceu!')
elif cpu == 2 and player == 1:
    print('\033[31m Computador venceu!')

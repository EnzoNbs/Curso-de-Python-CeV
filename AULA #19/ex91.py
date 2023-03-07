"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados num dicionário em Python. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter


jogo = dict()
rank = list()

jogo = {'Jogador 1': randint(1, 7),
        'Jogador 2': randint(1, 7),
        'Jogador 3': randint(1, 7),
        'Jogador 4': randint(1, 7)}

print('Rolando dados...')
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou [ {v} ]')

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('\nRanking dos jogadores: ')
for i, valor in enumerate(rank):
    print(f'{i+1}º Lugar: {valor[0]} com [ {valor[1]} ] pontos')
    sleep(1)

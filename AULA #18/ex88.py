"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep


jogo = []

print(f"\033[32m{'PALPITES PARA A MEGA SENA':^40}\033[0m\n{'_'*40}")
qtd = int(input('Quantos jogos você quer? '))
print(f'{f" Sorteando {qtd} jogos ":=^40}')

for j in range(0, qtd):
    while len(jogo) < 6:
        num = randint(0, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {j+1:>2}: {sorted(jogo)}')
    sleep(1)
    jogo.clear()
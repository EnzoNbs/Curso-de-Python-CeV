"""
Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 Peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador O programa deverá escrever na tela se o usuário venceu ou
perdeu
"""

from random import randint
from time import sleep

cpu = randint(0, 5)
print('-=-'*20)
print('Estou pensando em um número entre 0 e 5, Tente adivinhar!')
print('-=-'*20)

player = int(input('Em qual número estou pensando? '))
print('Processando...')
sleep(2)

if player == cpu:
    print(f'Você acertou! parabéns, o número era realmente o {cpu}.')
else:
    print(f'Você errou! na verdade, estava pensando no número {cpu}')

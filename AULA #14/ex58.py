"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.
"""

from random import randint


cpu = randint(0, 10)
tentativas = 0
certo = False

print('\033[1:36mEstou pensando em um número...\n Tente adivinhar!\033[0m')

while not certo:
    player = int(input('\033[1:33mEm que número pensei? \033[0m'))
    tentativas += 1
    if cpu == player:
        print(f'\033[32mVocê certou! Em {tentativas} tentativas.')
        certo = True
    else:
        if player > cpu:
            print('\033[31mÉ Menor, continue tentando!\n')
        else:
            print('\033[31mÉ Maior, continue tentando!\n')

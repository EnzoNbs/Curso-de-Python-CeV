"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
"""

from time import sleep
from random import randint


v = 0
print(f'\033[34m{" Vamos jogar PAR ou IMPAR ":=^40}\033[0m')

while True:
    cpu = randint(0, 10)
    print('[ P ] para PAR\n[ I ] para IMPAR')
    escolha = str(input('Escolha: ')).strip().upper()[0]

    while escolha not in "IiPp":
        escolha = str(input('\033[34mOpção inválida!'
                            '\033[0m\nEscolha I ou P: ')).strip().upper()[0]
    player = int(input('Digite um número(0 a 10): '))
    while player > 10 or player < 0:
        player = int(input('\033[34mEsse número não está entre 0 e 10'
                           '\033[0m\nDigite um número novamente: '))
    soma = cpu + player
    print(f'\n\033[31mComputador jogou [ {cpu} ]'
          f'\033[0m / \033[32mJogador jogou [ {player} ]\033[0m\n')
    sleep(1)
    print(f'A soma das jogadas é {soma}, este número é', end='')

    if soma % 2 == 0:
        print(f'\033[34m PAR')
        if escolha == "P":
            print('\033[32mJogador venceu! \n\033[0m')
            v += 1
        else:
            print('\033[31mComputador venceu!\033[0m')
            break
    elif soma % 2 != 0:
        print(f'\033[34m IMPAR')
        if escolha == "I":
            print('\033[32mJogador venceu! \n\033[0m')
            v += 1
        else:
            print('\033[31mComputador venceu!\033[0m')
            break
    sleep(1)
    print('Vamos jogar novamente...\n')
    sleep(1)

sleep(0.5)
if v == 0:
    print(f'\n\033[34mVocê não ganhou nenhuma vez')
elif v == 1:
    print(f'\n\033[34mVocê ganhou {v} vez')
else:
    print(f'\n\033[34mParabéns! você ganhou {v} vezes')

"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA mostrando os 10
primeiros termos da progressão usando a estrutura while.
"""

r = int(input('Digite a razão de uma P.A: '))
primeiro = int(input('Digite o primeiro termo: '))

decimo = primeiro + (10 - 1) * r

while primeiro <= decimo:
    print(f'{primeiro}', end='')
    print(f', ' if decimo > primeiro else '', end='')
    primeiro += r

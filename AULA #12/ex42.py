"""
Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""

r1 = int(input('Digite a primeira reta do triangûlo: '))
r2 = int(input('Digite a segunda reta do triangûlo: '))
r3 = int(input('Digite a terceira reta do triangûlo: '))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    if r3 == r2 == r1:
        print('As retas formam um triângulo '
              '\033[4:34mEquilátero\033[0m (Todos os lados iguais)')
    elif r3 == r1 != r2 or r3 == r2 != r1 or r1 == r2 != r3:
        print('As retas formam um triângulo '
              '\033[4:34mIsósceles\033[0m (Dois lados iguais)')
    elif r3 != r1 != r2:
        print('As retas formam um triângulo '
              '\033[4:34mEscaleno\033[0m (Todos os lados diferentes)')
else:
    print('\033[31mAs retas não formam um triângulo')

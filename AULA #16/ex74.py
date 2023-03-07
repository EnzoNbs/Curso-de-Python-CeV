"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.
"""

from random import randint


tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))

print(f'Valores sorteados: {tupla}')
print(f'O maior número sorteado é o {max(tupla)}\n'
      f'O Menor número sorteado é o {min(tupla)}')
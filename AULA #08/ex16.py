"""
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira.
"""

from math import trunc

num = float(input('Digite um número real: '))
print(f'O número {num} tem a sua parte inteira igual a {trunc(num)}')
# opcional: int(num)

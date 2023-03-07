"""
Faça um programa que leia um ângulo qualquer mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""

from math import cos, sin, tan, radians

ang = int(input('Digite um ângulo de um circulo: '))
rad = radians(ang)
print(f'Valor do seno: {sin(rad):.2f}')
print(f'Cosseno: {cos(rad):.2f}')
print(f'Tangente: {tan(rad):.2f}')

"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot

ca = float(input('Digite o tamanho do cateto adjacente: '))
co = float(input('Digite o tamanho do cateto oposto: '))
print(f'O tamanho da hipotenusa é {hypot(ca, co):.2f}')
# opcional: sqrt(pow(ca, 2) + (pow(co, 2)
# ou (ca ** 2 + co ** 2) ** 1/2

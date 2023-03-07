"""
Faça um programa que leia a largura e a altura de uma parede em metros
calcule a sua área e a quantidade de tinta necessária para pintá-la
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

alt = float(input('Digite a altura da parede em m²: '))
larg = float(input('Digite a largura da parede em m²: '))
area = larg * alt
print(f'A parede tem uma área de {area}m²')
print(f'Para pintar essa parede, será preciso {area/2}l de tinta')

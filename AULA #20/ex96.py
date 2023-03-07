"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def terreno(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno {largura} x {comprimento} é de {area:,.1f}m²')


print('Controle de Terrenos')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
terreno(larg, comp)


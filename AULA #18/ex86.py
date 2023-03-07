"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[], [], []]

for ln in range(0, 3):
    for col in range(0, 3):
        matriz[ln].append(int(input(f'Digite um Número para {ln, col}: ')))

for ln in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[ln][col]:^5}]', end='')
    print()

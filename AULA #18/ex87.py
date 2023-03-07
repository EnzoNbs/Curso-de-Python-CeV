"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[], [], []]
par_soma = ter_col_soma = maior_seg_ln = 0

for ln in range(0, 3):
    for col in range(0, 3):
        matriz[ln].append(int(input(f'Digite um Número para {ln, col}: ')))

    if ln == 1:
        if len(matriz[1]) == 0:
            maior_seg_ln = matriz[1][col]
        else:
            if matriz[1][col] > maior_seg_ln:
                maior_seg_ln = matriz[1][col]

ter_col = matriz[0][2] + matriz[1][2] + matriz[2][2]

for ln in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[ln][col]:^5}]', end='')

        if matriz[ln][col] % 2 == 0:
            par_soma += matriz[ln][col]
    print()

print(f'A) Soma de todos os pares digitados é {par_soma}')
print(f'B) A soma dos valores da terceira coluna é {ter_col}')
print(f'C) O maior valor da segunda linha é {maior_seg_ln}')  # max(matriz[1])

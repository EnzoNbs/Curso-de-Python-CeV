"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
"""

prods = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, \
    'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas',\
    22.30, 'Livro', 34.90

print(f'{"-"*40}\n{"Listagem de Preços":^40}\n{"-"*40}')
for i in range(0, len(prods), 2):
    print(f'{prods[i]:.<30}', end='')
    print(f'{"R$"}{prods[i+1]:>8.2f}')
print(f'{"-"*40}')
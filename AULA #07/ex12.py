"""
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto
"""

prod = float(input('Digite o preço do produto: R$'))
desconto = prod * 0.05
print('O produto obteve um desconto de 5% ')
print(f'Valor do desconto: R${desconto:.2f}')
print(f'Valor a pagar com o desconto: R$ {prod - desconto:.2f}')

"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

i = caros = total = menor = 0
barato = ''
print(f'{" Carrinho de Compras ":=^40}')

while True:
    nome = str(input('Nome do produto: ')).strip().title()
    prod = float(input('Preço do produto: R$'))
    i += 1
    total += prod

    if prod > 1000:
        caros += 1

    if i == 1:
        menor = prod
        barato = nome

    if prod < menor:
        barato = nome
        menor = prod

    opt = str(input('Quer adicionar mais produtos? [S/N] ')).strip().upper()[0]
    while opt not in "SsNn":
        opt = str(input('Quer adicionar mais produtos? [S/N]'
                        ' ')).strip().upper()[0]
    if opt == "N":
        break

print('-'*40)
print(f'A) Total da compra: R${total:.2f}\n'
      f'B) Quantos produtos custam mais de R$1000: {caros}\n'
      f'C) O produto mais barato: {barato} custando R${menor:.2f}')

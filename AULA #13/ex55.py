"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.
"""

maior = 0
menor = 0  # 9999

for i in range(0, 5):
    peso = float(input(f'Digite o peso da {i+1}º pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso informado {maior}Kg')
print(f'Menor peso informado {menor}Kg')

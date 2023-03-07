"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
mostre quantos dólares ela pode comprar.
"""

real = float(input('Digite o valor que deseja trocar por dolár: R$'))
# Cotação do dolár hoje: R$5,28
print(f'Valor recebido em dolár: US${real / 5.28:.2f}')

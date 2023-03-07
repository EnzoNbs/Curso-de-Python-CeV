"""
Escreva um programa que leia um valor em metros, exiba convertido em
centímetros e milímetros.
"""

metro = float(input('Digite um valor em metros: '))

print('Valor convertido em: ')
print(f'Quilômetro: {metro / 1000}')
print(f'Hectômetro: {metro / 100}')
print(f'Decâmetros: {metro / 10}')
print(f'Decímetros: {metro * 10:.0f}')
print(f'Centímetros: {metro * 100:.0f}')
print(f'Milímetros: {metro * 1000:.0f}')

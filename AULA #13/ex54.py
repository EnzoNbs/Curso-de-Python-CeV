"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date


maior = 0
menor = 0

for i in range(0, 7):
    nasc = int(input(f'Digite em que ano nasceu a {i+1}º pessoa: '))
    if date.today().year - nasc >= 21:  # Maioridade = 21 anos
        maior += 1
    else:
        menor += 1

print(f'\n{menor} pessoas são menores de idade '
      f'\ne {maior} pessoas ja são maiores de idade')

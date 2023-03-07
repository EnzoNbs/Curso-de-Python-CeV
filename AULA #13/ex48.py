"""
Faça um programa que calcule a soma entre todos os números que são múltiplos de
três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
cont = 0

for i in range(0, 501, 3):
    if i % 2 != 0:
        print(i, end=' ')
        soma += i
        cont += 1

print(f'\n\033[32mA soma de todos os {cont} números é {soma}')

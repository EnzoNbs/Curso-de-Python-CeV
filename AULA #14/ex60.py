"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""

num = int(input('Digite um número para descobrir o fatorial: '))
fat = 1
i = num
print(f'Resolução: fatorial de {num}!')

while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    fat *= i
    i -= 1
print(f'{fat}') # math.factorial()
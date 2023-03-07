"""Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo."""

num = int(input('Digite um número: '))
div = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1:32m', end='')
        div += 1
    else:
        print('\033[0m', end='')
    print(f'{c}', end=' ')

print(f'\n\033[0mO número {num} foi dividido {div} vezes')
if div == 2:
    print('Portanto, ele É PRIMO')
else:
    print('Portanto, ele NÃO É PRIMO')

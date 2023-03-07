"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados.
"""

num = str(input('Digite um número: '))
n = f'{num:0>4}'

print(f'O número {num} tem: ')
print(f'{n[3]} unidade(s)')
print(f'{n[2]} dezena(s)')
print(f'{n[1]} centena(s)')
print(f'{n[0]} milhar(es) ')
# u = num // 1 % 10
# c = num // 10 % 10
# d = num // 100 % 10
# m = num // 1000 % 10

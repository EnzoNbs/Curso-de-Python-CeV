"""
Escreva um programa que leia um número N inteiro qualquer e mostre na tela
os N primeiros elementos de uma Sequência de Fibonacci
"""

print(f'Sequência de Fibonacci\n{"-"*25}')
termos = int(input('Quantos termos deseja ver? '))
t1 = cont = 0
t2 = 1
print(f'{t1}, {t2}', end='')

while cont <= termos:
    cont += 1
    t3 = t2 + t1
    print(f', {t3}', end='')
    t1 = t2
    t2 = t3

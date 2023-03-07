"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
"""

frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
junto = ''.join(separar)
inv = ''  # inv = junto[::-1]

for i in range(len(junto) - 1, -1, -1):
    inv += junto[i]
print(f'O inverso de {junto} é {inv}')

if inv == junto:
    print('A frase é um palíndomo')
else:
    print('A frase não é um palíndromo')

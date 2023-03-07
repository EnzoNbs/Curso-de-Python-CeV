"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
"""

r = int(input('Digite a razão da P.A: '))
primeiro = int(input('Digite o primeiro termo: '))

decimo = primeiro + (10 - 1) * r

for i in range(primeiro, decimo + r, r):
    print(i, end=' ')

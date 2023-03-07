"""Faça um programa que leia um ano qualquer mostre se ele é bissexto."""

from datetime import date


print('Descubra se um ano é bissexto! (Digite 0 para o ano atual)')
ano = int(input('Digite o ano: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano BISSEXTO.')
else:
    print(f'{ano} NÃO é um ano BISSEXTO.')

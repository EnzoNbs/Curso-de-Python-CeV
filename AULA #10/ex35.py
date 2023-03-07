"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo."""

print('Digite o comprimento')
r1 = int(input('Da primeira reta do triângulo: '))
r2 = int(input('Da segunda reta do triângulo: '))
r3 = int(input('Da terceira reta do triângulo: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Todas as retas PODEM formar um triângulo.')
else:
    print('As retas NÃO formam um triângulo.')

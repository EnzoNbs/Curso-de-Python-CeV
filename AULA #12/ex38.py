"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na
tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 == n2:
    print('Os dois números são \033[34mIGUAIS')
elif n1 > n2:
    print('O \033[33mprimeiro número\033[0m é o\033[34m MAIOR')
else:
    print('O \033[33msegundo número\033[0m é o\033[34m MAIOR')

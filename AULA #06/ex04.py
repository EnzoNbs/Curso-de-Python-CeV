"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele.
"""

var = input('Digite algo para análise: ')

print(f'{"Tipo primitivo":25}\t{type(var)}')
print(f'{"É somente um espaço?":30}\t{var.isspace()}')
print(f'{"É um número?":30}\t{var.isnumeric()}')
print(f'{"É alfabético?":30}\t{var.isalpha()}')
print(f'{"É alfanumérico?":30}\t{var.isalpha()}')
print(f'{"Está em maiúsculas?":30}\t{var.isupper()}')
print(f'{"Está em minusculas?":30}\t{var.islower()}')
print(f'{"Está capitalizado?":30}\t{var.istitle()}')

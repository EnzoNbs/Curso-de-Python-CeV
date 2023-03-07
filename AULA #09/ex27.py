"""
Faça um programa que leia o nome completo de uma pessoa mostrando em  seguida
o primeiro e o último nome separadamente.
"""

nome = input('Digite um nome completo: ').strip().title()
partes = nome.split()

print(f'Nome completo: {nome}')
print(f'Primeiro nome: {partes[0]}')
print(f'Último nome: {partes[-1]}')

"""
Crie um programa que leia o nome de uma pessoa
e diga se ela tem “SILVA” no nome.
"""

name = input('Digite um nome: ').strip().title()
name = name.split()

print(f'Esse nome tem "Silva"? {"Silva" in name}')

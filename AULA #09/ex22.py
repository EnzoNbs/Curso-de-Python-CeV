"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras tem (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite o nome completo: ')).strip()

print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
print(f'O nome completo tem {len(nome.replace(" ", ""))} letras')
nome = nome.split()
print(f'O primeiro nome tem {len(nome[0])} letras')
# Opcional3: len(nome) - nome.count(' ')
# Opcional4: nome.find(' ')

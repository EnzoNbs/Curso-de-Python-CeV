"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não
com o nome “SANTO”.
"""

cidade = input('Digite o nome da cidade: ').strip().title()
cidade = cidade.split()

print(f'Essa cidade começa com "SANTO"? {"Santo" == cidade[0]}')

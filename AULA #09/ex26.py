"""
Faça um programa que leia uma frase pelo teclado mostre quantas vezes
aparece a letra “A”, em que posição ela aparece a primeira vez e em que
posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ').upper().strip()

print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A letra "A" aparece pela primeira vez na {frase.find("A")+1}° posição')
print(f'E aparece pela última vez na {frase.rfind("A")+1}° posição')

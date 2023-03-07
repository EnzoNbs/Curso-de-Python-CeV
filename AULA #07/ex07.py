"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e
mostre a sua média.
"""

n1 = float(input('Digite a nota do 1° Bimestre: '))
n2 = float(input('Digite a nota do 2° Bimestre: '))

media = (n1 + n2) / 2

print(f'Média das notas: {media:.1f}')

"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada.
"""

from random import shuffle

a1 = input('Digite o nome do primeiro alunos: ').strip().title()
a2 = input('Digite o nome do segundo aluno: ').strip().title()
a3 = input('Digite o nome de terceiro aluno: ').strip().title()
a4 = input('Digite o nome do quarto aluno: ').strip().title()
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de apresentação é a seguinte: {alunos}')

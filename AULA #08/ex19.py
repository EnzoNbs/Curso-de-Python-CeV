"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça
um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome
do escolhido.
"""

from random import choice

a1 = input('Digite o primeiro nome: ').strip().title()
a2 = input('Digite o segundo nome: ').strip().title()
a3 = input('Digite o terceiro nome: ').strip().title()
a4 = input('Digite o quarto nome: ').strip().title()
alunos = [a1, a2, a3, a4]
print(f'O Aluno escolhido para apagar o quadro é {choice(alunos)}')

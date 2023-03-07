"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
uma lista composta. No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = []
nota = []

while True:
    nome = str(input('Nome do Aluno: '))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    media = sum(nota) / len(nota)
    alunos.append([nome, nota[:], media])
    nota.clear()

    opt = str(input('Quer continuar [S/N]: '))
    while opt not in 'NnSs':
        opt = str(input('Quer continuar [S/N]: '))

    if opt in 'Nn':
        break

print(f'{"=-=" * 11}')
print(f'{"No.":<5}{"Nome":<20}{"Média":<5}')

for i, v in enumerate(alunos):
    print(f'{i:<5}{v[0]:<21}{v[2]}')

while True:
    ver = int(input('\nMostrar as notas de qual aluno? (999 interrompe): '))

    if ver == 999:
        break

    if ver <= len(alunos) - 1:
        print(f'Notas de {alunos[ver][0]} são as seguintes: {alunos[ver][1]}')

"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2
print(f'\nMédia do aluno: {media:.1f}')

if media < 5:
    print('Média abaixo de 5: aluno \033[31mReprovado!')
elif 5 <= media <= 6.9:
    print('Média entre 5 e 6.9: aluno de \033[34mRecuperação!')
else:
    print('Média 7 ou superior: aluno \033[32mAprovado!')

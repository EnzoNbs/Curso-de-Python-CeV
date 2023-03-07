"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No  final do
programa, mostre: a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos.
"""

nova = 0
idadeVelho = 0
soma = 0
maisVelho = "Ninguém"

for i in range(0, 4):
    print(f'\033[34m----- {i + 1}º Pessoa -----\033[0m')
    nome = str(input('Digite o nome da pessoa: ')).strip().title()
    idade = int(input('Digite a idade dessa pessoa: '))
    sx = str(input('Informe o sexo[M/F]: ')).upper().strip()
    soma += idade
    if sx == "M" and idade > idadeVelho:
        idadeVelho = idade
        maisVelho = nome
    if sx == "F" and idade < 20:
        nova += 1

media = soma/4
print(f'\nA média de idade do grupo é {media:.1f} anos')
print(f'O homem mais velho é {maisVelho} com {idadeVelho} anos')
print(f'São {nova} mulheres com menos de 20 anos')

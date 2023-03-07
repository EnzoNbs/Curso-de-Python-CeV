"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

print(f'{" Cadastro de pessoas ":=^40}')
maiores = h = f = 0

while True:
    idade = int(input('Informe a idade: '))
    sx = str(input('Informe o sexo: [F/M]: ')).strip().upper()[0]
    while sx not in "FfMm":
        sx = str(input('Informe o sexo: [F/M] ')).strip().upper()[0]
    print('-' * 25)

    opt = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opt not in "SsNn":
        opt = str(input('Quer continuar? [S/M] ')).strip().upper()[0]
    print('-' * 25)

    if idade >= 18:
        maiores += 1
    if sx == "M":
        h += 1
    if sx == "F" and idade < 20:
        f += 1
    if opt == "N":
        break

print(f'\nA) Quantidade de pessoas com mais de 18 anos: {maiores} \n'
      f'B) Quantidade de homens cadastrados: {h}\n'
      f'C) Quantidade de mulheres com menos de 20 anos: {f}\n')

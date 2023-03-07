"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa num dicionário e todos os dicionários numa lista. No
final, mostre:
 A) Quantas pessoas foram cadastradas
 B) A média de idade
 C) Uma lista com as mulheres
 D) Uma lista de pessoas com idade acima da média
"""

pessoa = {}
grupo = []
f_lista = []
AcimaDaMedia = []
SomaDasIdades = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('idade: '))

    grupo.append(pessoa.copy())
    SomaDasIdades += pessoa["idade"]

    print('=' * 40)
    while True:
        SN = str(input('Quer continuar? [S/N] ')).upper()[0]
        if SN in 'SN':
            break
    print('=' * 40)
    if SN in 'Nn':
        break

print(f'A) O grupo tem {len(grupo)} pessoa(s) cadastradas')

MediaDasIdades = SomaDasIdades / len(grupo)
print(f'B) A média de idade do grupo é {MediaDasIdades} anos')

for p in grupo:
    if p['sexo'] in 'Ff':  # p = feminino
        f_lista.append(pessoa['nome'])
print(f'C) Mulheres cadastradas: {"; ".join(f_lista)}')

for p in grupo:  # p = pessoa
    if p['idade'] > MediaDasIdades:
        AcimaDaMedia.append(p.copy())
print('\nD) Pessoas que estão acima da média:')

for p in AcimaDaMedia:  # p = pessoa
    print(f'Nome: {p["nome"]}; Sexo: {p["sexo"]}; Idade: {p["idade"]}')

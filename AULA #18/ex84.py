"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma
lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

dados = []
pessoas = []
pesado = []
leve = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    opt = str(input('Quer continuar? [S/N] '))
    while opt not in 'SsNn':
        opt = str(input('Quer continuar? [S/N] '))

    if opt in 'Nn':
        break

for p in pessoas:
    if p[1] == maior:
        pesado.append(p[0])
    elif p[1] == menor:
        leve.append(p[0])

print(f'Ao todo, Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de {", ".join(pesado)}.')
print(f'O menor peso foi de {menor}Kg. Peso de {", ".join(leve)}.')

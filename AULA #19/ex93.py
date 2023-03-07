"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
num dicionário, incluindo o total de gols feitos durante o campeonato
"""

jogador = dict()
gols = []

jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
Partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for i in range(0, Partidas):
    gols.append(int(input(f'Quantos gols na {i + 1}º partida: ')))
jogador['Gol(s)'] = gols[:]
jogador['Total'] = sum(gols)

print(f'{jogador}\n{"=-=" * 12}')
for k, v in jogador.items():
    print(f'{k}: {v}')

print('=-=' * 12)
print(f'Nome do Jogador: {jogador["Nome"]}')

for i, g in enumerate(gols):
    print(f'Na {i + 1}º partida, fez {g} gol(s) ')

print(f'Marcou {jogador["Total"]} gol(s) em {Partidas} partida(s)')
print(f'Média de Gols por partidas: {jogador["Total"] / Partidas}')

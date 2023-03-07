"""
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogador = dict()
time = list()

while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    Partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols = [] * Partidas
    for i in range(0, Partidas):
        gols.append(int(input(f'Quantos gols na {i + 1}º partida: ')))
    jogador['Gol(s)'] = gols
    jogador['Total'] = sum(gols)

    time.append(jogador.copy())

    print('===' * 20)
    while True:
        SN = str(input('Quer continuar? [S/N] ')).upper()[0]
        if SN in 'SN':
            break
    print('===' * 20)
    if SN in 'Nn':
        break

print(f'{"Nº":<3}{"Nome":<20}{"Gols":<20}{"Total":^7}')
for i, j in enumerate(time):
    print(f'{i:<3}{j["Nome"]:<20}{str(j["Gol(s)"]):<20}{j["Total"]:^7}')

while True:
    print('---'*20)
    print('Mostrar dados de jogador (999 para finalizar programa)')
    busca = int(input('Digite o Nº do jogador: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Nenhum jogador com código {busca}, tente novamente ')
    else:
        print(f'\n - Levantamento do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gol(s)']):
            print(f'Na {i + 1}º Partida, fez {g} gol(s)')

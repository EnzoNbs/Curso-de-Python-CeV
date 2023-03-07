"""
Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto():
    from datetime import datetime
    AnoAtual = datetime.now().year
    idade = AnoAtual - nasc
    if idade < 16:
        eleitor = 'NÃO VOTA'
    elif 16 <= idade < 65:
        eleitor = 'VOTO OBRIGATÓRIO'
    else:
        eleitor = 'VOTO OPCIONAL'
    print(f'Com {idade} anos: {eleitor}')


nasc = int(input('Em que ano você nasceu? '))
voto()

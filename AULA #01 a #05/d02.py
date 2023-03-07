"""Ler o dia, mês e o ano de nascimento de uma pessoa. Mostre uma mensagem com
a data formatada"""

dia = int(input('Que dia você nasceu? '))
mes = str(input('De que mês? ')).strip().capitalize()
ano = int(input('Em qual ano? '))

print(f'Você nasceu no dia {dia} de {mes}, em {ano}.')

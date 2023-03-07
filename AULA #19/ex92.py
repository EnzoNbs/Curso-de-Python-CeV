"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) num dicionário. Se por acaso a CTPS diferir de ZERO, o
dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date


individuo = dict()
individuo['Nome'] = str(input('Nome: ')).strip().title()
AnoDeNascimento = int(input('Ano de nascimento: '))
individuo['Idade'] = date.today().year - AnoDeNascimento
individuo['CTPS'] = int(input('Carteira de Trabalha (0 não tem): '))

if individuo['CTPS'] != 0:  # 35 anos de contribuição
    individuo['Contratado'] = int(input('Ano de contratação: '))
    individuo['Salário'] = int(input('Salário atual: R$'))
    AnosContribuidos = 35 - (date.today().year - individuo['Contratado'])
    individuo['Aposentadoria'] = AnosContribuidos + individuo['Idade']
else:
    individuo['CTPS'] = 'Não possui'

print()
for k, v in individuo.items():
    print(f'{k}: {v}')

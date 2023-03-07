"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
Desafio Extra: Incluir gênero
"""

from datetime import date


data = int(input('Informe o ANO de NASCIMENTO: '))
sexo = str(input('F para feminino, M para Masculino'
                 '\nInforme seu gênero: ')).upper().strip()
idade = date.today().year - data

print(f'\nQuem nasceu em {data} tem {idade} anos em {date.today().year}')

if idade == 18 and sexo == 'M':
    print('\033[32mVocê está no ano de se alistar ao serviço militar')
elif idade < 18 and sexo == 'M':
    print(f'\033[34mFalta {18 - idade} ano(s) para seu alistamento'
          f' no ano de {data + 18}')
elif idade > 18 and sexo == 'M':
    print(f'\033[31mSeu ano de alistamento foi em {data + 18},'
          f' você tem {idade - 18} ano(s) de atraso')
elif sexo == 'F':
    print('\033[36mPessoas do sexo feminino, não são obrigadas a se alistar')
    if idade >= 18:
        print('Entretanto você tem a idade para se voluntariar.')
    else:
        print(f'Você não tem a idade mínima,'
              f' mas se quiser, poderá se alistar em {data + 18}.')
else:
    print('Informações incorretas')

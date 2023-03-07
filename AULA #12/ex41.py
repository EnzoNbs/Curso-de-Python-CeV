"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

from datetime import date


ano = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - ano
print(f'\nIdade do atleta:{idade}')

if idade <= 9:
    print('Categoria: \033[34mMirim')
elif 9 < idade <= 14:
    print('Categoria: \033[34mInfantil')
elif 14 < idade <= 19:
    print('Categoria: \033[34mJunior')
elif 20 == idade:
    print('Categoria: \033[34mSênior')
else:
    print('Categoria: \033[34mMaster')

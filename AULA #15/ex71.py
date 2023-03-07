"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print(f'{"=" * 40}\n{"Caixa eletrônico":^40}\n{"=" * 40}')

while True:
    valor = int(input('\nQuanto você deseja sacar? R$'))
    print(f'Receba as seguintes cédulas:')
    total = valor
    c50 = total // 50
    total %= 50

    if c50 > 0:
        print(f'{c50} Nota(s) de R$50')
    c20 = total // 20
    total %= 20

    if c20 > 0:
        print(f'{c20} Nota(s) de R$20')
    c10 = total // 10
    total %= 10

    if c10 > 0:
        print(f'{c10} Nota(s) de R$10')
    c1 = total // 1
    total %= 1

    if c1 > 0:
        print(f'{c1} Nota(s) de R$1')
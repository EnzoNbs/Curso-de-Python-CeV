"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso. Extra: Pergunte se quer continuar
"""

extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',\
    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',\
    'dezesseis', "dezesste", 'dezoito', 'dezenove', 'vinte'
print('Números de 0 a 20 por extenso: ')

while True:
    num = int(input('Que número você quer ver extenso? '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}\n')

    opt = str(input('Quer ver mais? [S/N] ')).strip().upper()
    while opt not in "SsNn":
        opt = str(input('Quer ver mais? [S/N] ')).strip().upper()
    if opt == "N":
        break

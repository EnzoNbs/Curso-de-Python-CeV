"""
Escreva um programa em Python que leia um número inteiro qualquer. Peça para
o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input('Digite um número para conversão: '))
esc = int(input('Escolha uma base de conversão: \n'
                ' \033[4:34m[ 1 ]\033[0m para \033[1:34mbinário\033[0m\n'
                ' \033[4:34m[ 2 ]\033[0m para \033[1:34moctal\033[0m\n'
                ' \033[4:34m[ 3 ]\033[0m para \033[1:34mhexadecimal\033[0m\n'
                'Sua escolha: '))
if esc == 1:
    print(f'\nNúmero {num} na base Binária: {num:b}')
elif esc == 2:
    print(f'\nNúmero {num} na base Octal: {num:o}')
elif esc == 3:
    print(f'\nNúmero {num} na base hexadecimal {num:X}')
else:
    print('\nOpção incorreta, reinicie o programa.')

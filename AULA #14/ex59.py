"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior
[ 4 ] novos números [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

opt = 0

print('\033[1:34mDigite 2 números e escolha o tipo de cálculo.\033[0m')
num = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
print(f'\033[32m{" Menu de Operações ":=^40}\033[0m')
print(f'[ 1 ] Soma\n'
      f'[ 2 ] Multiplicar\n'
      f'[ 3 ] Maior número\n'
      f'[ 4 ] Trocar números\n'
      f'[ 5 ] Sair do programa')

while opt != 5:
    opt = int(input('\nTipo de cálculo: '))
    if opt == 4:
        print('Informe os números novamente')
        num = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opt == 1:
        res = num + num2
        print(f'\033[1:32mR: {num} + {num2} = {res}\033[0m')
    elif opt == 2:
        res = num * num2
        print(f'\033[1:32mR: {num} x {num2} = {res}\033[0m')
    elif opt == 3:
        res = max(num, num2)
        print(f'\033[1:32mO MAIOR número é o {res}\033[0m')
    elif opt == 5:
        print('\033[34mFinalizando programa...\033[0m')
    else:
        print('\033[1:31mOpção inválida! Tente novamente\033[0m')

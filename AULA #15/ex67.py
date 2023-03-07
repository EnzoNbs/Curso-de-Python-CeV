"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
"""

while True:
    num = int(input('Você quer ver a tabuada de que número? '))
    if num < 0:
        break
    print('-'*15)
    for i in range(1, 11):
        print(f' {num} x {i:2} = {num*i}')
    print('-' * 15)

print('Finalizando Programa...')

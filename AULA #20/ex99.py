"""
Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.
"""


from time import sleep


def MaiorNumero(*numeros):
    print('=-='*15)
    maior = cont = 0
    for i, v in enumerate(numeros):
        if i == 0:
            maior = v
        if v > maior:
            maior = v
        cont += 1
        print(v, end=' ')
        sleep(0.3)
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


MaiorNumero(2, 9, 4, 5, 7, 1)
MaiorNumero(4, 7, 0)
MaiorNumero(1, 2)
MaiorNumero(6)
MaiorNumero()

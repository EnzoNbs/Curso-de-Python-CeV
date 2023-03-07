"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
na lista e a segunda função vai mostrar a soma entre todos os valores pares
sorteados pela função anterior.
"""

from random import randint


numeros = list()


def sorteio():
    print(f'Números sorteados:', end=' ')
    for i in range(0, 5):
        num = randint(0, 10)
        print(f'{num}', end=' ')
        numeros.append(num)


def SomaPar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'\nSoma dos números pares {numeros} é {soma}')


sorteio()
SomaPar()

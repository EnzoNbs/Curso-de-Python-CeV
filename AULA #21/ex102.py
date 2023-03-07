"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um
valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.
"""


def fatorial(num, show=False):
    """
    — Calculo do fatorial de um número.
    :param num: Número a ser fatorado.
    :param show: (opcional) Mostrar a conta.
    :return: O valor do Fatorial do numéro n
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            if i > 1:
                print(f'{i} ', end='x ')
            else:
                print(f'{i} = ', end='')
    return f


print(f'{fatorial(5, True)}')
help(fatorial)
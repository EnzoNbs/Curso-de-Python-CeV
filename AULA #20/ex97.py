"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex:
escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~~
"""


def escreva(* frase):
    for i in frase:
        tamanho = i.center(len(i) + 4)
        print(f'{"~"* len(tamanho)}')
        print(f'{tamanho}')
        print(f'{"~" * len(tamanho)}')


escreva('Olá, Mundo')
escreva('Curso Em Video')
escreva('Curso de Pyton no Youtube')
escreva('CeV')

""" ex107
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.
''' ex108
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""
import moeda

val = float(input('Digite o valor: R$ '))
print(f'A metade é {moeda.moeda(moeda.metade(val))}')
print(f'O dobro é {moeda.moeda(moeda.dobro(val))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(val, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(val, 13))}')

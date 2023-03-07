"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um
parâmetro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda

val = float(input('Digite o valor: R$ '))
print(f'A metade é {moeda.metade(val, True)}')
print(f'O dobro é {moeda.dobro(val, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(val, 10, True)}')
print(f'Reduzindo 13% temos {moeda.diminuir(val, 13, True)}')

"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

c = A = E = I = O = U = 0

for i in range(c, len(tupla)):
    A = tupla[i].count('a')
    E = tupla[i].count('e')
    I = tupla[i].count('i')
    O = tupla[i].count('o')
    U = tupla[i].count('u')
    print(f'Na palavra {tupla[i]} tem: {"a " * A}{"e " * E}{"i " * I}{"o " * O}'
          f'{"u " * U}')

# Opcional: uso do for para cada palavra

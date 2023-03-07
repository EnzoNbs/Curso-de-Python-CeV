"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

num = int(input('Digite um número para gerar a tabuada: '))

print(f'\033[1:32m{"Tabuada":^20}\033[0m\n{"-=-"*7}')
for i in range(1, 11):
    print(f' {num} x {i:2} = {num*i:2}')

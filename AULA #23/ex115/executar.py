"""
criar um menu em Python, usando modularização.
"""

import ex115a
import ex115b
import ex115c

lista = 'ListadePessoas.txt'
if ex115b.verificarArquivo(lista):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    ex115b.criarArquivo(lista)

ex115a.menu()
while True:
    opt = ex115a.LerOpcoes('\033[36mSua opção: \033[0m')
    if opt == 1:
        ex115b.lerArquivo(lista)
    elif opt == 2:
        n = str(input('Nome: '))
        i = ex115c.LeiaInt('Idade: ')
        ex115c.cadastrar(lista, n, i)
    elif opt == 3:
        ex115a.sair()
        break

"""
Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
parênteses abertos e fechados na ordem correta.
"""

expressao = str(input('Digita a expressão para análise: ')).strip()
lista = []

for crtr in expressao:
    if crtr == '(':
        lista.append('(')
    elif crtr == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('A expressão é válida')
else:
    print('A expressão está errada!')

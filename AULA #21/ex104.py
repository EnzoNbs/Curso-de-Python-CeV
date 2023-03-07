"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante ‘a função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""


def LeiaInt(entrada):
    valido = False
    num = 0
    while True:
        numero = str(input(entrada))
        if numero.isnumeric():
            valido = True
            num = int(n)
        else:
            print('\033[31mERRO! Digite apenas um número inteiro\033[0m')
        if valido:
            break
    return num


n = LeiaInt('Digite um número: ')
print(f'Você digitou o número {n}')

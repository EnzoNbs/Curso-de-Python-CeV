"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação de um número de tipo inválido. Aproveite e crie
também uma função leiaFloat() com a mesma funcionalidade.
"""


def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido\033[0m')
        except KeyboardInterrupt:
            print('\033[34mEntrada de dados interrompida pelo usuário\033[0m')
            return 0
        else:
            return num


def LeiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número real válido\033[0m')
        except KeyboardInterrupt:
            print('\033[34mEntrada de dados interrompida pelo usuário\033[0m')
            return 0
        else:
            return num


inteiro = LeiaInt('Digite um número inteiro: ')
real = LeiaFloat('Digite um número Real: ')
print(f'\nO número inteiro digitado foi {inteiro}\nE o número real foi {real}')
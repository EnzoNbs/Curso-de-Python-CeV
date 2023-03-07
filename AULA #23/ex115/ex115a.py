def cabeçalho(msg):
    print(f'\033[34m{"-" * 40}')
    print(f'{msg:^40}')
    print(f'{"-" * 40}\033[0m')


def menu():
    cabeçalho('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')


def LerOpcoes(msg):
    print('-' * 40)
    try:
        opt = int(input(msg))
    except (TypeError, ValueError):
        print('\033[31mERRO: Digite um número inteiro válido\033[0m')
    except KeyboardInterrupt:
        print('\033[31mEscolha não informada...\033[0m')
    else:
        if opt > 3 or opt == 0:
            print('\033[31mERRO: Escolha uma opção válida\033[0m')
        else:
            return opt


def sair():
    cabeçalho('FINALIZANDO PROGRAMA')

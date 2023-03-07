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


def cadastrar(arqv, nome='Desconhecido', idade=0):
    try:
        doc = open(arqv, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            doc.write(f'{nome};{idade}\n')
        except:
            print('Erro no cadastro de pessoa')
        else:
            print(f'Novo registro de {nome} adicionado')
            doc.close()

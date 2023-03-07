def verificarArquivo(arqv):
    try:
        doc = open(arqv, 'rt')
        doc.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arqv):
    try:
        doc = open(arqv, 'wt+')
        doc.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arqv} criado com sucesso!')


def lerArquivo(arqv):
    try:
        doc = open(arqv, 'rt')
    except:
        print('Erro ao doc o arquivo')
    else:
        print('\033[32mPESSOAS CADASTRADAS\033[0m')
        for linha in doc:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

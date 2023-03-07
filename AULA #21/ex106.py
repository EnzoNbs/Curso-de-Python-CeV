"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM’, o programa se encerrará. Importante: use cores.
"""

c = ('\033[m',
     '\033[31m',
     '\033[32m',
     '\033[34m',
     '\033[:30:107m')


def ajuda(cmd):
    titulo(f'Acessando o manual do comando \'{cmd}\'', 3)
    print(c[4], end='')
    help(cmd)
    print(c[0], end='')


def titulo(frase, cor=0):
    tamanho = len(frase) + 4
    print(c[cor], end='')
    print(f'{"~"* tamanho}')
    print(f'  {frase}')
    print(f'{"~" * tamanho}')
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('PROGRAMA FINALIZADO')



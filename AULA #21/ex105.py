"""
Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""


def notas(*turma, sit=False):
    """
    — Função para analisar notas e situações de vários alunos.
    :param turma: uma ou mais notas dos alunos (aceita vários)
    :param sit: cpcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    info = {'Total': len(turma), 'Maior': max(turma), 'Menor': min(turma),
            'Média': sum(turma) / len(turma)}
    if sit:
        if info['Média'] < 5:
            info['Situação'] = 'RUIM'
        elif 5 <= info['Média'] < 7:
            info['Situação'] = 'RAZOÁVEL'
        else:
            info['Situação'] = 'BOA'
    return info


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)

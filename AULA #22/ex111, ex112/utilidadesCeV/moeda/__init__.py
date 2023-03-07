def aumentar(valor=0, porcentagem=0, formatar=False):
    res = valor + (valor * (porcentagem / 100))
    return res if formatar is False else moeda(res)


def diminuir(valor=0, porcentagem=0, formatar=False):
    res = valor - (valor * (porcentagem / 100))
    return res if formatar is False else moeda(res)


def dobro(valor=0, formatar=False):
    res = valor * 2
    return res if formatar is False else moeda(res)


def metade(valor=0, formatar=False):
    res = valor / 2
    return res if formatar is False else moeda(res)


def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:,.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao):
    print('~'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('~'*30)
    print(f'Valor Analisado: \t{moeda(valor)}')
    print(f'Dobro do Valor: \t{dobro(valor, True)}')
    print(f'Metade do Valor: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')

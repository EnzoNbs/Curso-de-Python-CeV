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


def moeda(val=0, simbolo='R$'):
    return f'{simbolo}{val:,.2f}'.replace('.', ',')


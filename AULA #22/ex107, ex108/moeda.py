def aumentar(valor=0, porcentagem=0):
    resultado = valor + (valor * (porcentagem / 100))
    return resultado


def diminuir(valor=0, porcentagem=0):
    resultado = valor - (valor * (porcentagem / 100))
    return resultado


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2


def moeda(val=0, simbolo='R$'):
    return f'{simbolo}{val:,.2f}'.replace('.', ',')

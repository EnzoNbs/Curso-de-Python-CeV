def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.')
        if valor.isalpha() or valor.strip() == "":
            print(f'\033[31mERRO: "{valor}" é um valor inválido!\033[0m')
        else:
            break
    return float(valor)
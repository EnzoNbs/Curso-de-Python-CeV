"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

print(f'\033[34m{" Caixa da Loja ":=^40}\033[0m')
valProduto = float(input('Digite o valor do produto: R$'))
forma = int(input('\033[32m FORMAS DE PAGAMENTO\033[0m\n'
                  '[ 1 ] para À vista no dinheiro\n'
                  '[ 2 ] para À vista no cartão\n'
                  '[ 3 ] para 2x no cartão sem juros\n'
                  '[ 4 ] para 3x ou mais no cartão'
                  '\nEscolha um opção de pagamento: '))
if forma == 1:
    print(f'\nÀ vista no dinheiro com desconto de 10%, '
          f'valor a pagar: R${valProduto - (valProduto * 0.10):.2f}')
elif forma == 2:
    print(f'\nÀ vista no cartão com desconto de 5%, '
          f'valor a pagar: R${valProduto - (valProduto * 0.05):.2f}')
elif forma == 3:
    print(f'\nNo cartão de crédito:\nEm 2x de R${(valProduto / 2):.2f}')
elif forma == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print('\nParcelado no cartão de crédito:')
    pagamento = (valProduto + (valProduto * 0.20)) / parcelas
    print(f'Em {parcelas}x de R${pagamento:.2f} com juros')
else:
    print('Opção de pagamento não listada!')

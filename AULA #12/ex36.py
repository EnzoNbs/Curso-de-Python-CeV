"""
Escreva um programa para aprovar o empréstimo bancário para a compra de
uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.
"""

valor = float(input('Digite o valor da casa: R$'))
anos = int(input('Quantos ANOS de finaciamento? '))
sal = float(input('Digite o salário do comprador: R$'))

prestacao = valor / (anos * 12)
limite = sal * 0.30

print(f'\nPrestações mensais: R${prestacao:.2f} durante {anos} anos')
if prestacao > limite:
    print('\033[1:31mEmpréstimo negado!')
else:
    print('\033[1:32mEmpréstimo aceito.')

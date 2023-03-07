"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor
do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    print('O funcionário recebeu um aumento de 10%.')
    aumento = salario + (salario * 0.10)
else:
    print('O funcionário recebeu um aumento de 15%.')
    aumento = salario + (salario * 0.15)

print(f'Seu novo salário é de R${aumento:.2f}')

"""
Faça um algoritmo que leia o salário de um funcionário
mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Digite o salário do funcionário: '))
aumento = salario * 0.15
print(f'Com um aumento de 15% equivalente a R${aumento:.2f}')
print(f'O novo salário será R${salario + aumento:.2f}')

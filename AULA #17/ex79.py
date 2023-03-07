"""
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.
"""

nums = list()

while True:
    n = int(input('Digite um número: '))
    if n not in nums:
        nums.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado, não vou adicionar')

    opt = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opt not in 'NnSs':
        opt = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opt in "Nn":
        break

print(f'Você digitou os valores {sorted(nums)}')

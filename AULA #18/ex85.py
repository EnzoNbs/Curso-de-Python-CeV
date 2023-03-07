"""
Crie um programa onde o usuário possa digitar sete valores numéricos cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.
"""

nums = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}° número: '))
    if num % 2 == 0:
        nums[0].append(num)
    elif num % 2 != 0:
        nums[1].append(num)

print(f'Números pares digitados: {sorted(nums[0])}\n'
      f'Números impares digitados: {sorted(nums[1])}')

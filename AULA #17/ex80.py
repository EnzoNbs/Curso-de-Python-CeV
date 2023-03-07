"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

nums = list()

nums.append(int(input('Digite um número: ')))

for i in range(0, 4):
    num = int(input('Digite um número: '))
    pos = 0
    if num > nums[-1]:
        nums.append(num)
    else:
        while pos < len(nums):
            if num <= nums[pos]:
                nums.insert(pos, num)
                break
            pos += 1

print(f'Número digitados em ordem: {nums}')

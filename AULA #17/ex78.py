"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
na lista.
"""

nums = list()
PosMaior = []
PosMenor = []

for i in range(0, 5):
    nums.append(int(input(f'Digite o {i+1}º número: ')))

for i, n in enumerate(nums):
    if n == max(nums):
        PosMaior.append(i)
    if n == min(nums):
        PosMenor.append(i)

print(f'Números digitados: {nums}')
print(f'O maior número digitado foi {max(nums)} nas posições: {PosMaior}')
print(f'O menor número digitado foi {min(nums)} nas posições: {PosMenor}')
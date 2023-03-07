"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

nums = (int(input(f'Digite um número: ')),
        int(input(f'Digite outro número: ')),
        int(input(f'Digite mais um número: ')),
        int(input(f'Digite o ultimo número: ')))

print(f'Quantas vezes o número 9 apareceu: {nums.count(9)}')

if 3 in nums:
    print(f'Posição que o número 3 apareceu: {nums.index(3)+1}º posição')
else:
    print(f'O número 3 não foi digitado')
print(f'Números pares:', end=' ')

for i in nums:
    if i % 2 == 0:
        print(f'{i}', end=' ')

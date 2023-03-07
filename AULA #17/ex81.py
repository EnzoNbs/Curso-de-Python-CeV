"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

nums = []

while True:
    nums.append(int(input('Digite um número: ')))

    opt = str(input('Quer continuar? [S/N] ')).strip()[0]
    while opt not in 'SsNn':
        opt = str(input('Quer continuar? [S/N] ')).strip()[0]
    if opt in 'Nn':
        break

nums.sort(reverse=True)

print(f'A) Quantos números foram digitados: {len(nums)}')
print(f'B) Os números em ordem decrescente: {nums}')

if 5 in nums:
    print(f'C) O número 5 faz parte da lista!')
else:
    print(f'C) O número 5 não faz parte da lista!')

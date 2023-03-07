"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, crie duas listas extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.
"""

nums = []
impar = []
par = []

while True:
    nums.append(int(input('Digite um número: ')))
    opt = str(input('Quer continuar? [S/N] '))
    while opt not in 'SsNn':
        opt = str(input('Quer continuar? [S/N] '))
    if opt in 'Nn':
        break

for num in nums:
    if num % 2 == 0:
        par.append(num)
    elif num % 2 != 0:
        impar.append(num)

print(f'Números digitados: {nums}')
print(f'Números pares: {par}')
print(f'Números impares: {impar}')
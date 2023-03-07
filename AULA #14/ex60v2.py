# Usando o for

num = int(input('Digite um número para determinar seu fatorial: '))
i = num
fat = 1
print(f'Resolução: fatorial de {num}!')

for i in range(num, 1, -1):
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    fat *= i
print(f'{fat}')

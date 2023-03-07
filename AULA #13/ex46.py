# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print(f'\033[1:31m{" Contagem regressiva ":!^40}\033[0m')
for i in range(10, -1, -1):
    sleep(0.5)
    print(i)
print('\033[1:31mFogo!')
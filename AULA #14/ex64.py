"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No
final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""

num = soma = cont = 0

print('\033[34mDigite vários números, para soma-los\n'
      'Caso queira encerrar o programa digite [ 999 ]\033[0m')
num = int(input('Digite um número: '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
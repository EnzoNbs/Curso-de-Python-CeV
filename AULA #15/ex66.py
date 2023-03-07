"""
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
"""

num = soma = cont = 0

print('\033[34mDigite vários números, para soma-los\n'
      'Caso queira encerrar o programa digite [ 999 ]\033[0m')
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Você digitou {cont} números e a soma deles é {soma}')

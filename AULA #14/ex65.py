"""
Crie um programa que leia vários números inteiros pelo teclado. No final da
execução, mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.
"""

opt = ""
soma = cont = maior = menor = 0

while opt != "N":
    num = int(input('Digite um número: '))
    opt = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if opt not in "NnSs":
        print('Opção inválida')
        continue
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num >= maior:
            maior = num
        if num <= menor:
            menor = num

print(f'Média de todos os {cont} números digitados é {soma/cont}')
print(f'MAIOR número é {maior} e o MENOR número é {menor}')

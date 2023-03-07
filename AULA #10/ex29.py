"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80Km/h. mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite.
"""

vel = float(input('Digite a velocidade atual do carro: '))

multa = (vel - 80)*7

if vel > 80:
    print('Você foi multado por exceder o limite de 80Km/h.')
    print(f'Valor da multa: R${multa:.2f}')
else:
    print('Você esta dentro do limite de velocidade de 80Km/h.')
    print('Continue assim e dirija com segurança.')
